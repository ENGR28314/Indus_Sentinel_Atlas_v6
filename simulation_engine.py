"""Simulation engines: basin stress, Water Quality Index, hazard clustering, rainfall/flash-flood synthesizer."""
from dataclasses import dataclass

WEATHER_POINTS = {  # region -> (basin, baseline rainfall mm/hr, catchment km2, runoff coeff)
    "Sialkot": ("Chenab", 8, 29000, 0.55),
    "Jhelum": ("Jhelum", 6, 33000, 0.50),
    "Lahore": ("Ravi", 7, 14400, 0.65),
}


def calculate_basin_stress(inflow_cumecs, demand_cumecs, installed_mw, operating_mw):
    """Stress index: demand/supply ratio (70%) weighted with power-plant loading (30%)."""
    if inflow_cumecs <= 0 or installed_mw <= 0:
        raise ValueError("inflow and installed capacity must be positive")
    return round(0.7 * demand_cumecs / inflow_cumecs + 0.3 * operating_mw / installed_mw, 3)


def water_quality_index(do_mgl, ph, tds_mgl, turbidity_ntu, ec_us):
    """Simplified 0-100 WQI from five parameters."""
    s_do = min(do_mgl / 8.0, 1) * 100
    s_ph = max(0, 100 - abs(ph - 7.2) * 30)
    s_tds = max(0, 100 - tds_mgl / 15)
    s_tur = max(0, 100 - turbidity_ntu * 2)
    s_ec = max(0, 100 - ec_us / 30)
    return round(0.25 * s_do + 0.15 * s_ph + 0.2 * s_tds + 0.15 * s_tur + 0.25 * s_ec, 1)


def wqi_status(wqi):
    if wqi >= 85: return "Excellent"
    if wqi >= 70: return "Good"
    if wqi >= 50: return "Poor"
    if wqi >= 30: return "Very Poor"
    return "Ecosystem Collapse Warning"


def rainfall_runoff_cumecs(rain_mm_hr, area_km2, c):
    """Rational method Q = C i A / 3.6 (i in mm/hr, A in km2)."""
    return c * rain_mm_hr * area_km2 / 3.6


def classify_hazard(flow_cumecs, rain_mm_hr):
    if flow_cumecs > 15000 or rain_mm_hr >= 50:
        return "Critical Hazard Warning"
    if flow_cumecs > 7000 or rain_mm_hr >= 20:
        return "Elevated"
    return "Nominal"


@dataclass
class FlashFloodResult:
    region: str
    basin: str
    rain_mm_hr: float
    peak_flow_cumecs: float
    stress_index: float
    status: str


def flash_flood_synthesizer(region, rain_mm_hr, channel_capacity_cumecs=12000):
    basin, _, area, c = WEATHER_POINTS[region]
    q = rainfall_runoff_cumecs(rain_mm_hr, area * 0.05, c)  # contributing fraction in short bursts
    return FlashFloodResult(region, basin, rain_mm_hr, round(q, 0), round(q / channel_capacity_cumecs, 3),
                            classify_hazard(q, rain_mm_hr))

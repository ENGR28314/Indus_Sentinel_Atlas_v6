"""Simple educational hydraulic tools: Manning flow, reservoir mass balance, travel time."""
import math
import pandas as pd


def manning_discharge(width_m, depth_m, slope, n=0.035):
    """Rectangular channel discharge (m3/s) using Manning's equation."""
    area = width_m * depth_m
    perim = width_m + 2 * depth_m
    r = area / perim
    return (1.0 / n) * area * r ** (2 / 3) * math.sqrt(slope)


def cumecs_to_cusecs(q):
    return q * 35.3147


def reservoir_simulation(initial_maf, capacity_maf, inflows_maf, releases_maf, dead_maf=0.0):
    """Monthly mass balance; returns DataFrame of storage, spill and shortage."""
    s, rows = initial_maf, []
    for i, (inf, rel) in enumerate(zip(inflows_maf, releases_maf), 1):
        s = s + inf - rel
        spill = max(0.0, s - capacity_maf)
        short = max(0.0, dead_maf - s)
        s = min(max(s, dead_maf), capacity_maf)
        rows.append(dict(month=i, inflow=inf, release=rel, storage=round(s, 3), spill=round(spill, 3), shortage=round(short, 3)))
    return pd.DataFrame(rows)


def flood_travel_time(distance_km, celerity_ms=2.0):
    """Hours for a flood wave to travel distance at given wave celerity."""
    return distance_km * 1000 / celerity_ms / 3600


# Indus reaches (km between control points) for travel-time demo
INDUS_REACHES = [
    ("Tarbela", "Jinnah", 190), ("Jinnah", "Chashma", 60), ("Chashma", "Taunsa", 270),
    ("Taunsa", "Guddu", 350), ("Guddu", "Sukkur", 150), ("Sukkur", "Kotri", 380),
]

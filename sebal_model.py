"""SEBAL - Surface Energy Balance Algorithm for Land (Bastiaanssen et al., 1998) for the Indus Basin.

Two layers:
  1. `sebal_numpy(...)` - pure NumPy implementation of the full SEBAL chain (works offline, unit-tested).
  2. `run_sebal_gee(...)` - Google Earth Engine pipeline on Landsat 8/9 Collection-2 Level-2 scenes,
     with the HydroSHEDS Indus basin boundary, geemap visualisation and geopandas sub-basin statistics.

Energy balance:  Rn = G + H + LE   ->   LE = Rn - G - H
Evaporative fraction  EF = LE / (Rn - G);   ET24 = EF * Rn24 * 86400 / lambda   (mm/day)
"""
from __future__ import annotations

import math
import numpy as np

SIGMA = 5.67e-8        # Stefan-Boltzmann (W m-2 K-4)
GSC = 1367.0           # solar constant (W m-2)
K_VON = 0.41           # von Karman
G_ACC = 9.81
RHO_AIR = 1.15         # kg m-3
CP = 1004.0            # J kg-1 K-1
LAMBDA = 2.45e6        # J kg-1
Z1, Z2, Z_BLEND = 0.1, 2.0, 200.0

INDUS_POINT = (71.0, 31.0)  # lon, lat inside the Indus plains (selects HydroSHEDS level-3 basin)
LANDSAT_SCALE_SR = (0.0000275, -0.2)
LANDSAT_SCALE_ST = (0.00341802, 149.0)


# ================= NumPy core (offline) =================
def albedo_landsat(blue, red, nir, swir1, swir2):
    """Liang (2001) broadband albedo from surface reflectance."""
    return np.clip(0.356 * blue + 0.130 * red + 0.373 * nir + 0.085 * swir1 + 0.072 * swir2 - 0.0018, 0.0, 1.0)


def vegetation_indices(red, nir, L=0.5):
    ndvi = (nir - red) / np.maximum(nir + red, 1e-6)
    savi = (1 + L) * (nir - red) / np.maximum(nir + red + L, 1e-6)
    lai = -np.log(np.clip((0.69 - savi) / 0.59, 1e-6, None)) / 0.91
    return ndvi, savi, np.clip(lai, 0.0, 6.0)


def emissivity(lai, ndvi):
    e0 = np.where(lai < 3, 0.95 + 0.01 * lai, 0.98)
    return np.where(ndvi < 0, 0.985, e0)


def solar_terms(doy, sun_elev_deg, elevation_m=200.0):
    dr = 1 + 0.033 * math.cos(2 * math.pi * doy / 365)
    tau = 0.75 + 2e-5 * elevation_m
    rs_in = GSC * math.cos(math.radians(90 - sun_elev_deg)) * dr * tau
    return rs_in, tau


def net_radiation(albedo, e0, ts, rs_in, tau, t_cold):
    ea = 0.85 * (-math.log(tau)) ** 0.09
    rl_in = ea * SIGMA * t_cold ** 4
    rl_out = e0 * SIGMA * ts ** 4
    return (1 - albedo) * rs_in + rl_in - rl_out - (1 - e0) * rl_in


def soil_heat_flux(rn, ts, albedo, ndvi):
    tc = ts - 273.15
    ratio = tc / np.maximum(albedo, 1e-3) * (0.0038 * albedo + 0.0074 * albedo ** 2) * (1 - 0.98 * ndvi ** 4)
    return np.where(ndvi < 0, 0.5 * rn, ratio * rn)


def roughness(savi):
    return np.exp(-5.809 + 5.62 * savi)


def _psi(L, z):
    """Monin-Obukhov stability corrections psi_m, psi_h (unstable: Paulson; stable: -5 z/L)."""
    L = np.where(np.abs(L) < 1e-6, -1e-6, L)
    x = np.where(L < 0, np.abs(1 - 16 * z / L) ** 0.25, 1.0)
    psi_m = np.where(L < 0, 2 * np.log((1 + x) / 2) + np.log((1 + x ** 2) / 2) - 2 * np.arctan(x) + 0.5 * np.pi, -5 * z / L)
    psi_h = np.where(L < 0, 2 * np.log((1 + x ** 2) / 2), -5 * z / L)
    return psi_m, psi_h


def select_anchor_pixels(ndvi, ts, albedo):
    """Cold = dense well-watered vegetation (high NDVI, low Ts); hot = dry bare soil (low NDVI, high Ts)."""
    flat = np.arange(ndvi.size)
    n, t = ndvi.ravel(), ts.ravel()
    veg = flat[n >= np.nanpercentile(n, 95)]
    cold = veg[np.argmin(t[veg])]
    bare = flat[(n <= np.nanpercentile(n, 10)) & (n > 0) & (albedo.ravel() > 0.15)]
    if bare.size == 0:
        bare = flat[n <= np.nanpercentile(n, 10)]
    hot = bare[np.argmax(t[bare])]
    return np.unravel_index(cold, ndvi.shape), np.unravel_index(hot, ndvi.shape)


def sensible_heat(rn, g, ts, savi, cold, hot, u_ref=2.5, z_ref=2.0, iterations=8):
    """Iterative SEBAL H with dT = a + b*Ts calibrated at hot (LE=0) and cold (H=0) pixels."""
    z0m_w = 0.12 * 0.3
    u_star_w = K_VON * u_ref / math.log(z_ref / z0m_w)
    u200 = u_star_w * math.log(Z_BLEND / z0m_w) / K_VON
    z0m = roughness(savi)
    u_star = K_VON * u200 / np.log(Z_BLEND / z0m)
    rah = np.log(Z2 / Z1) / (u_star * K_VON)
    h_hot = rn[hot] - g[hot]
    a = b = 0.0
    h = np.zeros_like(rn)
    for _ in range(iterations):
        dt_hot = h_hot * rah[hot] / (RHO_AIR * CP)
        b = dt_hot / (ts[hot] - ts[cold])
        a = -b * ts[cold]
        h = RHO_AIR * CP * (a + b * ts) / rah
        L = -RHO_AIR * CP * u_star ** 3 * ts / (K_VON * G_ACC * np.where(np.abs(h) < 1e-3, 1e-3, h))
        psi_m200, _ = _psi(L, Z_BLEND)
        _, psi_h2 = _psi(L, Z2)
        _, psi_h1 = _psi(L, Z1)
        u_star = K_VON * u200 / np.maximum(np.log(Z_BLEND / z0m) - psi_m200, 0.5)
        rah = np.maximum((np.log(Z2 / Z1) - psi_h2 + psi_h1) / (u_star * K_VON), 1.0)
    return np.clip(h, 0, None), float(a), float(b)


def sebal_numpy(blue, red, nir, swir1, swir2, ts, doy, sun_elev, elevation_m=200.0, u_ref=2.5):
    """Full SEBAL chain; returns dict of arrays (Rn, G, H, LE, EF, ET_inst mm/h, ET24 mm/day) + anchors."""
    alb = albedo_landsat(blue, red, nir, swir1, swir2)
    ndvi, savi, lai = vegetation_indices(red, nir)
    e0 = emissivity(lai, ndvi)
    cold, hot = select_anchor_pixels(ndvi, ts, alb)
    rs_in, tau = solar_terms(doy, sun_elev, elevation_m)
    rn = net_radiation(alb, e0, ts, rs_in, tau, ts[cold])
    g = soil_heat_flux(rn, ts, alb, ndvi)
    h, a, b = sensible_heat(rn, g, ts, savi, cold, hot, u_ref)
    h = np.minimum(h, rn - g)
    le = np.clip(rn - g - h, 0, None)
    ef = np.clip(le / np.maximum(rn - g, 1e-3), 0, 1)
    rs24 = rs_in / max(math.cos(math.radians(90 - sun_elev)), 0.2) * 0.32
    rn24 = (1 - alb) * rs24 - 110 * tau          # de Bruin (1987)
    et24 = np.clip(ef * rn24 * 86400 / LAMBDA, 0, 15)
    return dict(albedo=alb, ndvi=ndvi, lai=lai, Rn=rn, G=g, H=h, LE=le, EF=ef,
                ET_inst=3600 * le / LAMBDA, ET24=et24, cold=cold, hot=hot, a=a, b=b)


def synthetic_indus_scene(n=120, seed=7):
    """Synthetic Landsat-like scene: irrigated canal command (left), desert (right), river strip."""
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 1, n)[None, :].repeat(n, 0)
    veg = np.clip(1.2 - 1.6 * x + rng.normal(0, 0.08, (n, n)), 0, 1)
    river = np.abs(np.arange(n)[:, None] - (0.5 * n + 8 * np.sin(np.arange(n)[None, :] / 9))) < 2
    red = 0.05 + 0.20 * (1 - veg)
    nir = 0.18 + 0.30 * veg
    red, nir = np.where(river, 0.04, red), np.where(river, 0.02, nir)
    blue, swir1, swir2 = red * 0.8, 0.12 + 0.2 * (1 - veg), 0.08 + 0.18 * (1 - veg)
    ts = np.where(river, 298.0, 300.0 + 22 * (1 - veg) + rng.normal(0, 0.7, (n, n)))
    return dict(blue=blue, red=red, nir=nir, swir1=swir1, swir2=swir2, ts=ts)


# ================= Google Earth Engine pipeline =================
def init_ee(project: str | None = None):
    import ee
    try:
        ee.Initialize(project=project)
    except Exception:
        ee.Authenticate()
        ee.Initialize(project=project)
    return ee


def indus_basin(ee):
    """HydroSHEDS level-3 basin containing the Indus plains."""
    return ee.FeatureCollection("WWF/HydroSHEDS/v1/Basins/hybas_3").filterBounds(ee.Geometry.Point(*INDUS_POINT))


def landsat_collection(ee, region, start, end, max_cloud=20):
    def prep(img):
        sr = img.select(["SR_B2", "SR_B4", "SR_B5", "SR_B6", "SR_B7"]).multiply(LANDSAT_SCALE_SR[0]).add(LANDSAT_SCALE_SR[1])
        st = img.select("ST_B10").multiply(LANDSAT_SCALE_ST[0]).add(LANDSAT_SCALE_ST[1]).rename("Ts")
        qa = img.select("QA_PIXEL")
        clear = qa.bitwiseAnd(1 << 3).eq(0).And(qa.bitwiseAnd(1 << 4).eq(0))
        return (sr.rename(["blue", "red", "nir", "swir1", "swir2"]).addBands(st).updateMask(clear)
                .copyProperties(img, ["system:time_start", "SUN_ELEVATION"]))
    col = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2").merge(ee.ImageCollection("LANDSAT/LC09/C02/T1_L2"))
    return col.filterBounds(region).filterDate(start, end).filter(ee.Filter.lt("CLOUD_COVER", max_cloud)).map(prep)


def sebal_ee_image(ee, img, region, u_ref=2.5, scale=300, iterations=3):
    """Apply SEBAL to one prepared Landsat ee.Image -> bands Rn, G, H, LE, EF, ET24, ndvi, albedo."""
    img = ee.Image(img)
    elevation = ee.Image("USGS/SRTMGL1_003")
    doy = ee.Date(img.get("system:time_start")).getRelative("day", "year").add(1)
    sun = ee.Number(img.get("SUN_ELEVATION"))
    b = {k: img.select(k) for k in ["blue", "red", "nir", "swir1", "swir2", "Ts"]}
    alb = img.expression("0.356*b+0.130*r+0.373*n+0.085*s1+0.072*s2-0.0018",
                         dict(b=b["blue"], r=b["red"], n=b["nir"], s1=b["swir1"], s2=b["swir2"])).clamp(0, 1).rename("albedo")
    ndvi = img.normalizedDifference(["nir", "red"]).rename("ndvi")
    savi = img.expression("1.5*(n-r)/(n+r+0.5)", dict(n=b["nir"], r=b["red"])).rename("savi")
    lai = savi.multiply(-1).add(0.69).divide(0.59).max(1e-6).log().multiply(-1 / 0.91).clamp(0, 6)
    e0 = lai.multiply(0.01).add(0.95).where(lai.gte(3), 0.98).where(ndvi.lt(0), 0.985)
    ts = b["Ts"]
    tau = elevation.multiply(2e-5).add(0.75)
    dr = doy.multiply(2 * math.pi / 365).cos().multiply(0.033).add(1)
    cos_z = ee.Number(90).subtract(sun).multiply(math.pi / 180).cos()
    rs_in = tau.multiply(cos_z.multiply(GSC).multiply(dr))

    red_kw = dict(geometry=region, scale=scale, maxPixels=1e10, bestEffort=True)
    stats = ndvi.addBands(ts).reduceRegion(ee.Reducer.percentile([10, 95]), **red_kw)
    cold_mask = ndvi.gte(ee.Number(stats.get("ndvi_p95")))
    hot_mask = ndvi.lte(ee.Number(stats.get("ndvi_p10"))).And(ndvi.gt(0))
    t_cold = ee.Number(ts.updateMask(cold_mask).reduceRegion(ee.Reducer.percentile([5]), **red_kw).get("Ts"))
    t_hot = ee.Number(ts.updateMask(hot_mask).reduceRegion(ee.Reducer.percentile([95]), **red_kw).get("Ts"))
    hot_px = hot_mask.And(ts.gte(t_hot))

    ea = tau.log().multiply(-1).pow(0.09).multiply(0.85)
    rl_in = ea.multiply(SIGMA).multiply(ee.Image.constant(t_cold).pow(4))
    rn = (alb.multiply(-1).add(1).multiply(rs_in).add(rl_in).subtract(e0.multiply(SIGMA).multiply(ts.pow(4)))
          .subtract(e0.multiply(-1).add(1).multiply(rl_in)).rename("Rn"))
    g = img.expression("(T-273.15)/a*(0.0038*a+0.0074*a*a)*(1-0.98*pow(v,4))*R",
                       dict(T=ts, a=alb.max(1e-3), v=ndvi, R=rn)).where(ndvi.lt(0), rn.multiply(0.5)).rename("G")

    z0m_w = 0.036
    u200 = u_ref * math.log(Z_BLEND / z0m_w) / math.log(2 / z0m_w)
    z0m = savi.multiply(5.62).add(-5.809).exp()
    log_blend = ee.Image.constant(Z_BLEND).divide(z0m).log()
    u_star = ee.Image.constant(K_VON * u200).divide(log_blend)
    rah = ee.Image.constant(math.log(Z2 / Z1)).divide(u_star.multiply(K_VON))
    avail_hot = ee.Number(rn.subtract(g).rename("A").updateMask(hot_px).reduceRegion(ee.Reducer.mean(), **red_kw).get("A"))
    h = ee.Image.constant(0)
    for _ in range(iterations):
        rah_hot = ee.Number(rah.rename("r").updateMask(hot_px).reduceRegion(ee.Reducer.mean(), **red_kw).get("r"))
        dt_hot = avail_hot.multiply(rah_hot).divide(RHO_AIR * CP)
        bb = dt_hot.divide(t_hot.subtract(t_cold))
        aa = bb.multiply(t_cold).multiply(-1)
        h = ts.multiply(bb).add(aa).multiply(RHO_AIR * CP).divide(rah).max(0)
        L = u_star.pow(3).multiply(ts).multiply(-RHO_AIR * CP).divide(h.max(1e-3).multiply(K_VON * G_ACC))
        def x_of(z):
            return ee.Image.constant(1).subtract(ee.Image.constant(16 * z).divide(L)).abs().pow(0.25)
        x200, x2, x1 = x_of(Z_BLEND), x_of(Z2), x_of(Z1)
        psi_m200 = img.expression("2*log((1+x)/2)+log((1+x*x)/2)-2*atan(x)+0.5*3.14159", dict(x=x200))
        psi_h2 = x2.pow(2).add(1).divide(2).log().multiply(2)
        psi_h1 = x1.pow(2).add(1).divide(2).log().multiply(2)
        u_star = ee.Image.constant(K_VON * u200).divide(log_blend.subtract(psi_m200).max(0.5))
        rah = ee.Image.constant(math.log(Z2 / Z1)).subtract(psi_h2).add(psi_h1).divide(u_star.multiply(K_VON)).max(1)
    h = h.min(rn.subtract(g)).rename("H")
    le = rn.subtract(g).subtract(h).max(0).rename("LE")
    ef = le.divide(rn.subtract(g).max(1e-3)).clamp(0, 1).rename("EF")
    rs24 = rs_in.multiply(0.32).divide(cos_z.max(0.2))
    rn24 = alb.multiply(-1).add(1).multiply(rs24).subtract(tau.multiply(110))
    et24 = ef.multiply(rn24).multiply(86400 / LAMBDA).clamp(0, 15).rename("ET24")
    return ee.Image.cat([rn, g, h, le, ef, et24, ndvi, alb]).copyProperties(img, ["system:time_start"])


def run_sebal_gee(project, start, end, max_cloud=20, scale=300, u_ref=2.5):
    """Returns (ee module, Indus basin FeatureCollection, mean ET24 image, number of scenes)."""
    ee = init_ee(project)
    basin = indus_basin(ee)
    region = basin.geometry()
    col = landsat_collection(ee, region, start, end, max_cloud)
    et = col.map(lambda im: sebal_ee_image(ee, im, ee.Image(im).geometry().intersection(region, 100), u_ref=u_ref, scale=scale))
    return ee, basin, et.select("ET24").mean().clip(region), col.size().getInfo()


def ee_fc_to_gdf(fc):
    """ee.FeatureCollection -> geopandas GeoDataFrame (geemap if available, else GeoJSON via getInfo)."""
    import geopandas as gpd
    try:
        import geemap
        return geemap.ee_to_gdf(fc)
    except Exception:
        return gpd.GeoDataFrame.from_features(fc.getInfo()["features"], crs=4326)


def subbasin_stats_gdf(ee, et_img, basin, scale=1000):
    """geopandas GeoDataFrame of mean ET24 per HydroSHEDS level-5 sub-basin inside the Indus."""
    subs = ee.FeatureCollection("WWF/HydroSHEDS/v1/Basins/hybas_5").filterBounds(basin.geometry())
    fc = et_img.reduceRegions(subs, ee.Reducer.mean().setOutputs(["ET24_mean"]), scale)
    gdf = ee_fc_to_gdf(fc.select(["HYBAS_ID", "SUB_AREA", "ET24_mean"]))
    gdf = gdf.set_crs(4326, allow_override=True)
    return add_volume_columns(gdf)


def add_volume_columns(gdf):
    """Area (km2, UTM 42N) and daily ET volume (million m3/day) for a GeoDataFrame with ET24_mean."""
    gdf = gdf.copy()
    gdf["area_km2"] = gdf.to_crs(32642).area / 1e6
    gdf["ET_volume_MCM_day"] = gdf["ET24_mean"].fillna(0) * gdf["area_km2"] / 1000
    return gdf


ET_VIS = {"min": 0, "max": 8, "palette": ["d7191c", "fdae61", "ffffbf", "a6d96a", "1a9641", "2b83ba"]}


def gee_map(ee, et_img, basin):
    """Folium map with Earth Engine tile layers (geemap-style), works across geemap versions."""
    import folium
    m = folium.Map(location=[31, 71], zoom_start=5)
    for img, vis, name in [(et_img, ET_VIS, "SEBAL ET24 (mm/day)"),
                           (ee.Image().paint(basin, 0, 2), {"palette": ["000000"]}, "Indus Basin (HydroSHEDS)")]:
        tiles = ee.Image(img).getMapId(vis)["tile_fetcher"].url_format
        folium.TileLayer(tiles=tiles, attr="Google Earth Engine", name=name, overlay=True).add_to(m)
    folium.LayerControl().add_to(m)
    return m

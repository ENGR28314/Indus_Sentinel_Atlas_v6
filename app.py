"""Indus Sentinel: Pakistan Hydro-Strategic & Disaster Risk Atlas - Streamlit app.
Run:  streamlit run app.py
"""
import streamlit as st
import plotly.express as px
from streamlit_folium import st_folium

import data_loader as dl
import hazards as hz
import domains as dm
import hydraulic_model as hm
import simulation_engine as se
import forests_parks as fp
import sustainability as sus
import references as refs
import agro_inputs as ai
import indian_projects as ip
import folium
import maps_extra as mx
import pandas as pd
from map_view import build_map, LAYERS
from network_view import build_network

st.set_page_config(page_title="Indus Sentinel", page_icon="🌊", layout="wide")
st.title("🇵🇰 Indus Sentinel: Pakistan Hydro-Strategic & Disaster Risk Atlas")
st.markdown("**Created and Designed by: Engr. Syed Hassan Iqbal Shah**")
st.caption("Educational reference. Figures are approximate and compiled from public sources.")

PAGES = ["🗺️ Map", "🏞️ Provinces", "🌊 Rivers & Infrastructure", "🔀 Indus Network", "🌡️ Climatic Regions",
         "⛰️ Mountain Ranges", "💧 Lakes", "⚠️ Disaster Risk Context", "📈 Socio-Economic", "🌾 Agro-Economic",
         "🗺️ Geo-Political & Strategic", "⚖️ IRSA Legal Mechanisms", "🏗️ China Hydropower", "📐 Pakal Dul & Ratle / CoA",
         "🧮 Hydraulic Tools", "🌲 Forests", "🏕️ National Parks", "🇮🇳 Indian Atrocities",
         "🌦️ Live Weather & Flash Floods", "📈 Gauge Telemetry", "🧪 Water Quality & Basin Stress",
         "🎯 UN SDGs, MDGs & Vision 2030", "🛰️ SEBAL Evapotranspiration", "🗺️ 17 Indian Hydro Projects (CEA)", "🤖 AI ET Review", "📚 Sources"]
page = st.sidebar.radio("Navigate", PAGES)
st.sidebar.markdown("---")
st.sidebar.markdown("**Created and Designed by:**  \nEngr. Syed Hassan Iqbal Shah")


def show_dict(d):
    for k, v in d.items():
        with st.expander(k, expanded=False):
            if isinstance(v, dict):
                show_dict(v)
            elif isinstance(v, list):
                for i in v:
                    st.markdown(f"- {i}")
            else:
                st.write(v)


def input_driven(key):
    st.subheader("Input-driven socio/agro data")
    st.caption("Edit the figures below (sample values) - the chart updates.")
    df = st.data_editor(ai.DEFAULT_INPUT, num_rows="dynamic", use_container_width=True, key=f"ed_{key}")
    c1, c2 = st.columns(2)
    g = c1.selectbox("Graph type", ai.GRAPH_TYPES, key=f"g_{key}")
    m = c2.selectbox("Metric", list(ai.METRICS), key=f"m_{key}")
    st.plotly_chart(ai.make_chart(df, g, m), use_container_width=True)


if page == PAGES[0]:
    layers = st.multiselect("Layers", list(LAYERS), default=list(LAYERS))
    st_folium(build_map(layers, st.checkbox("Show rivers", True)), width=None, height=650)
    st.dataframe(dl.points_df(), use_container_width=True)

elif page == PAGES[1]:
    p = st.selectbox("Province / Region", list(dl.PROVINCES))
    info = dl.PROVINCES[p]
    c1, c2 = st.columns(2)
    c1.metric("Capital", info["capital"]); c2.metric("Climate", info["climate"])
    st.markdown(f"**Rivers:** {', '.join(info['rivers'])}")
    st.markdown(f"**Dams / HPPs:** {', '.join(info['dams'])}")
    st.markdown(f"**Mountain ranges:** {', '.join(info['ranges'])}")
    st.info(info["notes"])

elif page == PAGES[2]:
    st.subheader("Rivers (upstream source -> downstream mouth)")
    st.dataframe(dl.RIVERS, use_container_width=True)
    st.plotly_chart(px.bar(dl.RIVERS, x="River", y="Length_km"), use_container_width=True)
    st.subheader("Dams"); st.dataframe(dl.DAMS_TABLE, use_container_width=True)
    st.subheader("Barrages / Headworks"); st.write(", ".join(dl.BARRAGES))
    st.subheader("Link Canals"); st.dataframe(dl.LINK_CANALS, use_container_width=True)
    st.subheader("River Confluences"); st.write(", ".join(dl.CONFLUENCES))
    st.subheader("Link Canals — Indus Basin Irrigation System (IBIS)")
    st_folium(mx.link_canals_map(), height=520, width=None, key="lc_map")

elif page == PAGES[3]:
    st.plotly_chart(build_network(), use_container_width=True)
    st.plotly_chart(mx.irrigation_hydropower_schematic(), use_container_width=True)
    st.plotly_chart(mx.confluence_schematic(), use_container_width=True)

elif page == PAGES[4]:
    st.dataframe(dl.CLIMATE_REGIONS, use_container_width=True)
    st.subheader("Climatic Regions of Pakistan (map)")
    st_folium(mx.climate_map(), height=520, width=None, key="clim_map")

elif page == PAGES[5]:
    group = st.radio("Group", list(dl.MOUNTAINS), horizontal=True)
    rng = st.selectbox("Range", list(dl.MOUNTAINS[group]))
    r = dl.MOUNTAINS[group][rng]
    st.header(rng); st.metric("Highest Peak", r["peak"])
    for label, key in [("Other notable peaks", "other"), ("Surrounding areas", "surroundings"),
                       ("Rivers flowing through", "rivers"), ("Climbing details", "climbing"),
                       ("Geological information", "geology"), ("Tourist guide", "guide")]:
        st.markdown(f"**{label}:** {r[key]}")

elif page == PAGES[6]:
    prov = st.multiselect("Province", sorted(dl.LAKES_TABLE.Province.unique()))
    df = dl.LAKES_TABLE if not prov else dl.LAKES_TABLE[dl.LAKES_TABLE.Province.isin(prov)]
    st.dataframe(df, use_container_width=True)
    st.plotly_chart(px.histogram(dl.LAKES_TABLE, x="Province"), use_container_width=True)

elif page == PAGES[7]:
    t1, t2, t3, t4 = st.tabs(["1. Hazard Profile", "2. Exposure & Vulnerability", "3. Emerging Risks", "4. Risk Scenarios"])
    with t1: show_dict(hz.HAZARD_PROFILE)
    with t2: show_dict(hz.VULNERABILITY)
    with t3: show_dict(hz.EMERGING_RISKS)
    with t4: st.table(hz.SCENARIOS)
    st.subheader("Historical Events & Hazards Map")
    st_folium(mx.historical_events_map(), height=550, width=None, key="hist_map")

elif page == PAGES[8]:
    show_dict(dm.SOCIO_ECONOMIC)
    input_driven("socio")

elif page == PAGES[9]:
    show_dict(dm.AGRO_ECONOMIC)
    st.plotly_chart(px.bar(dm.CROPS, x="Crop", y="Production_Mt_approx", color="Season"), use_container_width=True)
    st.subheader("Major crop seasons")
    st.markdown("**Rabi** (winter, sown Oct-Dec, harvested Apr-May) and **Kharif** (summer, sown Apr-Jun, harvested Oct-Nov).")
    st.markdown("**Rabi**"); st.dataframe(ai.RABI, use_container_width=True)
    st.markdown("**Kharif**"); st.dataframe(ai.KHARIF, use_container_width=True)
    st.subheader("Apiculture"); st.dataframe(ai.APICULTURE, use_container_width=True)
    st.subheader("Aquaculture"); st.dataframe(ai.AQUACULTURE, use_container_width=True)
    input_driven("agro")

elif page == PAGES[10]:
    st.subheader("Geo-Political & Strategic"); show_dict(dm.GEOPOLITICS)
    st.subheader("Environmental Impacts of Indian Chenab Projects on Punjab's Crops"); show_dict(dm.CHENAB_IMPACTS)
    st.subheader("CPEC Infrastructure Investment: Diamer-Bhasha Dam"); show_dict(dm.DIAMER_BHASHA)
    st.subheader("Internal Inter-Provincial Water Disputes: Punjab vs Sindh"); show_dict(dm.PROVINCIAL_DISPUTE)
    st.subheader("Geo-Political & Strategic map")
    st_folium(mx.geopolitical_map(), height=550, width=None, key="geo_map")

elif page == PAGES[11]:
    show_dict(dm.LEGAL_MECHANISMS)

elif page == PAGES[12]:
    show_dict(dm.CHINA_HYDRO)
    st.subheader("Major Hydropower Asset Portfolios")
    st.dataframe(dm.HYDRO_ASSETS, use_container_width=True)
    st.plotly_chart(px.pie(dm.HYDRO_ASSETS, names="Project", values="Capacity_MW"), use_container_width=True)
    st.metric("Total capacity", f"{dm.HYDRO_ASSETS.Capacity_MW.sum():,.1f} MW")
    st.subheader("Chinese-backed hydropower map")
    st_folium(mx.china_hydro_map(), height=500, width=None, key="cn_map")

elif page == PAGES[13]:
    for dam, pts in dm.INDIA_DESIGNS.items():
        st.header(dam)
        for point, (issue, view) in pts.items():
            with st.expander(point):
                st.markdown(f"**The Issue:** {issue}"); st.markdown(f"**Pakistan's View:** {view}")
    st.header("The Court of Arbitration (CoA) Interventions")
    for e in dm.COA_INTERVENTIONS + ip.COA_TIMELINE_ADDITIONS:
        st.markdown(f"- {e}")
    st.subheader("Indian projects on the western rivers (map)")
    st_folium(mx.india_projects_map(), height=500, width=None, key="in_map")

elif page == PAGES[14]:
    st.subheader("Manning's equation (rectangular channel)")
    c = st.columns(4)
    w = c[0].number_input("Width (m)", 1.0, 2000.0, 100.0); d = c[1].number_input("Depth (m)", 0.1, 50.0, 4.0)
    s = c[2].number_input("Slope", 0.00001, 0.05, 0.0002, format="%.5f"); n = c[3].number_input("n", 0.01, 0.1, 0.035)
    q = hm.manning_discharge(w, d, s, n)
    st.success(f"Q = {q:,.0f} m³/s  ≈ {hm.cumecs_to_cusecs(q):,.0f} cusecs")
    st.subheader("Reservoir mass balance (Tarbela-like, MAF)")
    inflow = [0.5, 0.5, 0.8, 1.5, 3.5, 6.0, 9.0, 8.0, 3.5, 1.2, 0.7, 0.6]
    rel = st.slider("Uniform monthly release (MAF)", 0.5, 6.0, 3.0)
    df = hm.reservoir_simulation(4.0, 13.69, inflow, [rel] * 12, dead_maf=1.0)
    st.plotly_chart(px.line(df, x="month", y=["storage", "spill", "shortage"]), use_container_width=True)
    st.subheader("Flood wave travel time along Indus")
    cel = st.slider("Wave celerity (m/s)", 0.5, 5.0, 2.0)
    st.table([{"From": a, "To": b, "km": k, "hours": round(hm.flood_travel_time(k, cel), 1)} for a, b, k in hm.INDUS_REACHES])
    st.subheader("Interactive Hydraulic & Risk Model map")
    c1, c2 = st.columns(2)
    rr = c1.slider("Rainfall (mm/hr)", 0, 100, 20, key="rk_rain"); ff = c2.slider("River flow factor", 0.0, 2.0, 1.0, key="rk_flow")
    st_folium(mx.risk_map(rr, ff), height=520, width=None, key="risk_map")

elif page == PAGES[15]:
    st.subheader("Main Forest Types in Pakistan"); show_dict(fp.FOREST_TYPES)
    st.subheader("Notable Forests")
    f = st.selectbox("Select a forest", list(fp.FORESTS))
    prov, la, lo, area, hist, wild, attr = fp.FORESTS[f]
    st.markdown(f"**Location:** {prov}  \n**Covered area:** {area}  \n**History & origin:** {hist}  \n"
                f"**Wildlife & nature:** {wild}  \n**Attractions & recreation:** {attr}")
    fm = folium.Map([la, lo], zoom_start=10); folium.Marker([la, lo], tooltip=f, icon=folium.Icon(color="green", icon="tree-conifer")).add_to(fm)
    st_folium(fm, height=420, width=None, key="forest_map")

elif page == PAGES[16]:
    p = st.selectbox("Select a park for details", list(fp.PARKS))
    prov, la, lo, area, info = fp.PARKS[p]
    c1, c2 = st.columns(2); c1.metric("Province", prov); c2.metric("Area", area)
    st.info(info)
    pm = folium.Map([la, lo], zoom_start=12)
    folium.Marker([la, lo], tooltip=p, popup=f"{p} - {area}", icon=folium.Icon(color="darkgreen", icon="leaf")).add_to(pm)
    folium.Circle([la, lo], radius=1500, color="green", fill=True, fill_opacity=0.15).add_to(pm)
    st_folium(pm, height=450, width=None, key="park_map")
    st.subheader("All parks")
    st.map(pd.DataFrame([{"lat": v[1], "lon": v[2]} for v in fp.PARKS.values()]))

elif page == PAGES[17]:
    st.header("Chenab Projects, Flow Concerns and the Indus Waters Treaty")
    st.caption("Presents Pakistan's stated position.")
    show_dict(ip.CANALS)
    st.subheader("2(A). The Disputed Engineering Specifications")
    st.write("Pakistan argues India's designs go beyond the run-of-the-river permissions of the IWT, building 'imagined capacity' for structural control over transboundary flows.")
    for k, (icon, d, disp, conc) in ip.DISPUTED_SPECS.items():
        with st.expander(f"{icon} {k}"):
            st.markdown(f"{d}\n\n**The Dispute:** {disp}\n\n**The Strategic Concern:** {conc}")
    st.plotly_chart(px.bar(pd.DataFrame(ip.PONDAGE_CHART), x="Project", y="MCM", color="Party", barmode="group", title="Pondage: design vs Pakistan's cap"), use_container_width=True)
    st.subheader("2(B). Neutral Expert Timeline (Michel Lino)")
    for d, e in ip.NEUTRAL_EXPERT_SCHEDULE:
        st.markdown(f"**{d}** - {e}  \n⬇️")
    st.subheader("The Incompatible Reality on the Ground"); show_dict(ip.GROUND_REALITY)
    st.subheader("Mapped: 17 Official Indian Indus-Basin Hydro Projects in J&K")
    st.caption("India's Central Electricity Authority (CEA), 15 Jun 2026: 10 operational and 7 under construction.")
    cea = pd.DataFrame(ip.CEA_PROJECTS, columns=["No", "Project", "River", "District", "MW", "Status", "lat", "lon"])
    k = st.columns(3)
    k[0].metric("Operational", f"{(cea.Status == 'Operational').sum()} projects", f"{cea[cea.Status == 'Operational'].MW.sum():,.0f} MW")
    k[1].metric("Under construction", f"{(cea.Status != 'Operational').sum()} projects", f"{cea[cea.Status != 'Operational'].MW.sum():,.1f} MW")
    k[2].metric("Total", f"{cea.MW.sum():,.1f} MW")
    status = st.multiselect("Show", ["Operational", "Under construction"], default=["Operational", "Under construction"], key="cea_f")
    view = cea[cea.Status.isin(status)]
    cm = folium.Map([33.7, 75.0], zoom_start=8)
    for r in view.itertuples():
        col = "#1f4e9c" if r.Status == "Operational" else "#e8761b"
        folium.CircleMarker([r.lat, r.lon], radius=6 + r.MW / 120, color=col, fill=True, fill_opacity=0.8,
                            tooltip=f"{r.No}. {r.Project} - {r.MW} MW", popup=f"{r.Project}<br>{r.River}, {r.District}<br>{r.MW} MW<br>{r.Status}").add_to(cm)
    st_folium(cm, height=520, width=None, key="cea_map")
    st.caption("Positions are approximate (schematic placement by district and river).")
    st.dataframe(view.drop(columns=["lat", "lon"]), use_container_width=True, hide_index=True)
    st.plotly_chart(px.bar(view, x="Project", y="MW", color="Status", color_discrete_map={"Operational": "#1f4e9c", "Under construction": "#e8761b"}), use_container_width=True)
    st.info(ip.CEA_NOTE)
    import os
    img = os.path.join(os.path.dirname(__file__), "assets", "indian_hydro_projects_jk.jpg")
    if os.path.exists(img):
        st.image(img, caption="Reference map. Sources: CEA, Profile on Hydro Development for U.T. of J&K (15 Jun 2026); NHPC. Image (c) Mind Over Mic.")

elif page == PAGES[18]:
    region = st.selectbox("Region (basin point)", list(se.WEATHER_POINTS))
    basin, base, _, _ = se.WEATHER_POINTS[region]
    st.caption(f"{region} maps to the {basin} basin. Baseline rainfall {base} mm/hr (simulated).")
    rain = st.slider("Rainfall intensity (mm/hr)", 0, 100, base)
    r = se.flash_flood_synthesizer(region, rain)
    c = st.columns(3); c[0].metric("Peak runoff", f"{r.peak_flow_cumecs:,.0f} m³/s"); c[1].metric("Basin strain", r.stress_index); c[2].metric("Status", r.status)
    {"Nominal": st.success, "Elevated": st.warning}.get(r.status, st.error)(f"{r.status} for the {basin} basin")

elif page == PAGES[19]:
    df = dl.telemetry_12_months()
    gauges = st.multiselect("Gauges", list(dl.GAUGES), default=list(dl.GAUGES)[:2])
    st.plotly_chart(px.area(df, x="date", y=gauges, title="12-month simulated water levels (m)"), use_container_width=True)

elif page == PAGES[20]:
    st.subheader("Water Quality Index")
    c = st.columns(5)
    w = se.water_quality_index(c[0].number_input("DO mg/L", 0.0, 15.0, 7.5), c[1].number_input("pH", 0.0, 14.0, 7.4),
        c[2].number_input("TDS mg/L", 0, 5000, 300), c[3].number_input("Turbidity NTU", 0, 200, 5), c[4].number_input("EC µS/cm", 0, 10000, 450))
    st.metric("WQI", w, se.wqi_status(w))
    st.subheader("Basin stress")
    c = st.columns(4)
    s_ = se.calculate_basin_stress(c[0].number_input("Inflow m³/s", 1, 50000, 5000), c[1].number_input("Demand m³/s", 0, 50000, 3500),
        c[2].number_input("Installed MW", 1, 10000, 4888), c[3].number_input("Operating MW", 0, 10000, 3000))
    st.metric("Stress index", s_, "High" if s_ > 0.8 else "OK")

elif page == PAGES[21]:
    st.subheader("Millennium Development Goals (2000-2015)"); st.dataframe(sus.MDGS, use_container_width=True)
    st.subheader("UN Sustainable Development Goals (2030 Agenda)"); st.dataframe(sus.SDGS, use_container_width=True)
    st.subheader("Vision 2030 agenda"); show_dict(sus.VISION_AGENDA)

elif page == "📚 Sources":
    for t, u in refs.SOURCES:
        st.markdown(f"- [{t}]({u})")

elif page == PAGES[22]:
    import sebal_model as sb
    st.header("SEBAL - Surface Energy Balance Algorithm for Land (Indus Basin)")
    st.markdown("Energy balance **Rn = G + H + LE**. Crop water use (evapotranspiration) is the energy left for evaporation, LE. "
                "**EF = LE/(Rn-G)**, **ET24 = EF x Rn24 x 86400 / lambda** (mm/day). Hot (dry, LE=0) and cold (wet, H=0) "
                "anchor pixels calibrate dT = a + b*Ts, with Monin-Obukhov stability iterations.")
    t1, t2 = st.tabs(["Offline demo (no login)", "Google Earth Engine (real Landsat)"])
    with t1:
        c = st.columns(4)
        doy = c[0].slider("Day of year", 1, 365, 180); sun = c[1].slider("Sun elevation (deg)", 20, 80, 65)
        u = c[2].slider("Wind at 2 m (m/s)", 0.5, 8.0, 2.5); n = c[3].select_slider("Grid size", [60, 120, 200], 120)
        r = sb.sebal_numpy(**sb.synthetic_indus_scene(n), doy=doy, sun_elev=sun, u_ref=u)
        k = st.columns(4)
        k[0].metric("Mean ET24", f"{r['ET24'].mean():.2f} mm/day"); k[1].metric("Max ET24", f"{r['ET24'].max():.2f} mm/day")
        k[2].metric("Mean Rn", f"{r['Rn'].mean():.0f} W/m2"); k[3].metric("dT = a + b*Ts", f"a={r['a']:.1f}, b={r['b']:.3f}")
        band = st.selectbox("Layer", ["ET24", "EF", "Rn", "G", "H", "LE", "ndvi", "albedo"])
        fig = px.imshow(r[band], color_continuous_scale="RdYlGn" if band in ("ET24", "EF", "LE", "ndvi") else "Inferno",
                        title=f"{band} - synthetic scene (irrigated left, desert right, river strip)")
        fig.add_scatter(x=[int(r["cold"][1])], y=[int(r["cold"][0])], mode="markers", marker=dict(color="blue", size=14, symbol="x"), name="cold pixel")
        fig.add_scatter(x=[int(r["hot"][1])], y=[int(r["hot"][0])], mode="markers", marker=dict(color="red", size=14, symbol="x"), name="hot pixel")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Synthetic data for learning the method. Use the Earth Engine tab for real Indus Basin results.")
    with t2:
        st.markdown("Needs a free Google Earth Engine account and a registered Google Cloud project. Run `earthengine authenticate` once on your computer.")
        c = st.columns(4)
        proj = c[0].text_input("GEE Cloud project ID", "")
        start = c[1].date_input("Start", pd.Timestamp("2025-05-01")); end = c[2].date_input("End", pd.Timestamp("2025-06-30"))
        cloud = c[3].slider("Max cloud %", 5, 60, 20)
        if st.button("Run SEBAL on Earth Engine", disabled=not proj):
            try:
                with st.spinner("Processing Landsat 8/9 scenes over the Indus Basin..."):
                    ee, basin, et, nimg = sb.run_sebal_gee(proj, str(start), str(end), cloud)
                    st.success(f"{nimg} Landsat scenes used.")
                    st_folium(sb.gee_map(ee, et, basin), height=600, width=None, key="sebal_map")
                    st.caption("Colour scale: red 0 to blue 8 mm/day.")
                    gdf = sb.subbasin_stats_gdf(ee, et, basin)
                    st.subheader("Sub-basin ET (HydroSHEDS level 5, via geopandas)")
                    st.dataframe(gdf.drop(columns="geometry"), use_container_width=True)
                    st.download_button("Download sub-basin ET (GeoJSON)", gdf.to_json(), "indus_sebal_et.geojson")
            except ImportError as e:
                st.error(f"Missing package: {e.name}. Run: pip install -r requirements.txt")
            except Exception as e:
                st.error(f"Earth Engine error: {e}")

elif page == PAGES[23]:
    st.header("The 17 projects by India on waterways of the Indus River System")
    st.markdown("India has **10 operational** and **7 under-construction** hydropower projects across the Indus basin in Jammu & Kashmir, "
                "drawn from India's Central Electricity Authority (CEA) data. Total **6,911.5 MW**: **3,360 MW** operational and **3,551.5 MW** under construction.")
    cea = pd.DataFrame(ip.CEA_PROJECTS, columns=["No", "Project", "River", "District", "MW", "Status", "lat", "lon"])
    cea["River channel"] = cea.Project.map(ip.CEA_CHANNELS)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Operational Projects (10)**")
        for line in ip.CEA_DESC_OPERATIONAL: st.markdown(f"- {line}")
    with c2:
        st.markdown("**Under-Construction Projects (7)**")
        for line in ip.CEA_DESC_UC: st.markdown(f"- {line}")
    sep = folium.Map([33.7, 75.0], zoom_start=8, tiles="OpenStreetMap")
    for grp_name, color in [("Operational", "#1f4e9c"), ("Under construction", "#e8761b")]:
        fg = folium.FeatureGroup(name=f"{grp_name} ({(cea.Status == grp_name).sum()})")
        for r in cea[cea.Status == grp_name].itertuples():
            folium.CircleMarker([r.lat, r.lon], radius=7 + r.MW / 110, color=color, fill=True, fill_opacity=0.85,
                                tooltip=f"{r.No}. {r.Project} - {r.MW:g} MW",
                                popup=folium.Popup(f"<b>{r.Project}</b><br>{r._9}<br>{r.District}<br>{r.MW:g} MW<br>{r.Status}", max_width=260)).add_to(fg)
            folium.Marker([r.lat, r.lon], icon=folium.DivIcon(html=f"<div style='font-size:10px;font-weight:700;color:#fff;margin:-6px 0 0 -4px'>{r.No}</div>")).add_to(fg)
        fg.add_to(sep)
    folium.LayerControl(collapsed=False).add_to(sep)
    st_folium(sep, height=620, width=None, key="cea_sep_map")
    st.caption("Positions are approximate (schematic placement by district and river).")
    for grp_name, title in [("Operational", "Operational Projects (3,360 MW)"), ("Under construction", "Under-Construction Projects (3,551.5 MW)")]:
        st.subheader(title)
        st.dataframe(cea[cea.Status == grp_name][["Project", "MW", "River channel"]].rename(columns={"MW": "Capacity (MW)"}),
                     use_container_width=True, hide_index=True)
    st.caption("Sources: CEA, Profile on Hydro Development for U.T. of J&K (15 Jun 2026); NHPC project pages; R. Akhtar (LinkedIn post).")


elif page == "🤖 AI ET Review":
    import ai_review as ar
    st.header("AI Review of SEBAL Evapotranspiration Results")
    st.markdown("Water managers submit SEBAL ET results per sub-basin. Rule checks flag unusual values and an AI model "
                "explains water-use patterns. AI output is advisory - verify before decisions.")
    with st.form("et_submit", clear_on_submit=True):
        c1, c2, c3 = st.columns(3)
        b = c1.selectbox("Sub-basin", list(ar.SUB_BASINS))
        d = c2.date_input("Image date")
        lu = c3.selectbox("Dominant land use", ["Irrigated cropland", "Rainfed", "Rangeland", "Forest", "Barren/desert", "Mixed"])
        c4, c5, c6 = st.columns(3)
        m = c4.number_input("Mean ET (mm/day)", 0.0, 20.0, 3.0, 0.1)
        mx = c5.number_input("Max ET (mm/day)", 0.0, 25.0, 6.0, 0.1)
        a = c6.number_input("Area (km2)", 0.0, 1e6, 1000.0, 10.0)
        n = st.text_input("Notes (cloud cover, sensor, etc.)")
        if st.form_submit_button("Submit result"):
            ar.save_submission(dict(sub_basin=b, date=str(d), mean_et_mm_day=m, max_et_mm_day=mx,
                                    area_km2=a, land_use=lu, notes=n))
            st.success("Result saved.")
    up = st.file_uploader("Or upload CSV (columns: " + ", ".join(ar.COLUMNS) + ")", type="csv")
    if up is not None and st.button("Add uploaded rows"):
        for row in pd.read_csv(up).to_dict(orient="records"):
            ar.save_submission({k: row.get(k, "") for k in ar.COLUMNS})
        st.success("Uploaded rows saved.")
    df = ar.load_submissions()
    if df.empty:
        st.info("No submissions yet.")
    else:
        sel = st.multiselect("Sub-basins to review", sorted(df.sub_basin.unique()), default=sorted(df.sub_basin.unique()))
        view = ar.flag_values(df[df.sub_basin.isin(sel)])
        st.metric("Flagged records", f"{(view.issues != '').sum()} of {len(view)}")
        st.dataframe(view.style.apply(lambda r: ["background-color: #ffe0e0" if r.issues else "" for _ in r], axis=1),
                     use_container_width=True)
        st.plotly_chart(px.box(view, x="sub_basin", y="mean_et_mm_day", points="all", title="Mean ET by sub-basin"),
                        use_container_width=True)
        if st.button("Explain with AI", disabled=view.empty):
            try:
                st.write_stream(ar.stream_explanation(view))
            except ar.GatewayError as e:
                st.error(str(e))
            except Exception:
                st.error("Could not reach the AI service. Check your internet connection and try again.")

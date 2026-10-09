"""Thematic interactive maps (Folium) and schematic networks (Plotly) for each domain."""
import folium
import plotly.graph_objects as go
from coordinates import BARRAGES, CONFLUENCES, RIVER_PATHS, DAMS

# name: (lat, lon, colour, note)
GEOPOLITICAL = {
    "Line of Control (approx.)": (34.30, 74.00, "red", "Disputed Kashmir boundary; western rivers cross here"),
    "Kishanganga HEP (India)": (34.65, 74.75, "darkred", "Diverts Neelum/Kishanganga waters"),
    "Baglihar HEP (India)": (33.18, 75.33, "darkred", "Chenab; flow drops reported at Marala"),
    "Salal HEP (India)": (33.15, 74.80, "darkred", "Chenab, upstream of Marala"),
    "Head Marala": (32.67, 74.46, "orange", "Chenab entry point into Pakistan"),
    "Diamer-Bhasha Dam (CPEC)": (35.52, 73.74, "green", "Strategic storage on the Indus"),
    "Karachi Port": (24.84, 66.98, "blue", "Main seaport"),
    "Port Qasim": (24.77, 67.33, "blue", "Industrial & energy port"),
    "Gwadar Port (CPEC)": (25.12, 62.33, "blue", "Deep-sea port, CPEC gateway"),
    "Khunjerab Pass (China border)": (36.85, 75.42, "purple", "CPEC overland link via KKH"),
    "Guddu-Sukkur (Sindh share)": (27.68, 68.85, "cadetblue", "Punjab vs Sindh flashpoint (lower riparian)"),
    "Taunsa-Panjnad Link": (30.51, 70.85, "cadetblue", "Disputed link canal operations"),
}

CHINA_HYDRO = {
    "Karot HPP (720 MW)": (33.61, 73.60, "In operation (2022) - CTG"),
    "Suki Kinari HPP (884 MW)": (34.83, 73.50, "In operation (2024) - CGGC"),
    "Kohala HPP (1,124 MW)": (34.10, 73.50, "Planned - CTG"),
    "Azad Pattan HPP (700.7 MW)": (33.73, 73.58, "Planned - CGGC"),
    "Diamer-Bhasha Dam (Power China-FWO)": (35.52, 73.74, "Under construction"),
    "Dasu HPP (CGGC contractor)": (35.29, 73.21, "Under construction"),
}

INDIA_PROJECTS = {
    "Pakal Dul (1,000 MW)": (33.45, 75.82, "Marusudar (Chenab trib.) - pondage/freeboard disputed"),
    "Ratle (850 MW)": (33.32, 75.75, "Chenab - CoA concrete freeze (Aug 2026)"),
    "Kiru (624 MW)": (33.38, 75.88, "Chenab"),
    "Kwar (540 MW)": (33.40, 75.85, "Chenab"),
    "Kishanganga (330 MW)": (34.65, 74.75, "Neelum - 2013 Court of Arbitration award"),
    "Baglihar (900 MW)": (33.18, 75.33, "Chenab"),
    "Head Marala (Pakistan)": (32.67, 74.46, "Downstream impact point"),
}

HISTORICAL_EVENTS = {
    "2005 Kashmir Earthquake M7.6": (34.49, 73.63, "earthquake", "~86,000 deaths"),
    "2010 Super Flood": (28.00, 69.50, "flood", "20M affected"),
    "2022 Floods": (26.50, 68.00, "flood", "33M affected, ~1,700 deaths"),
    "2010 Attabad Landslide Lake": (36.32, 74.86, "landslide", "Blocked Hunza River"),
    "2025 Taalidass GLOF (Ghizer)": (36.20, 73.50, "glof", "Glacial lake outburst"),
    "2015 Karachi Heatwave": (24.86, 67.01, "heat", "1,200+ deaths"),
    "1945 Makran Tsunami": (25.26, 63.47, "tsunami", "M8.1, Pasni/Ormara"),
    "2013 Awaran Earthquake M7.7": (26.95, 65.50, "earthquake", "~400 deaths"),
    "2012 Gayari Avalanche": (35.30, 76.70, "avalanche", "140 buried"),
    "2022 Murree Snowstorm": (33.91, 73.39, "snow", "Tourists trapped"),
    "2001 Islamabad Cloudburst": (33.68, 73.05, "flood", "620 mm in 10 hrs"),
    "2023 Cyclone Biparjoy": (24.10, 67.80, "cyclone", "Coastal evacuation"),
    "Lahore Smog (seasonal)": (31.55, 74.34, "smog", "AQI > 500"),
    "1998-2002 Balochistan Drought": (28.50, 65.50, "drought", "Severe livestock loss"),
}
EVENT_COLORS = {"earthquake": "darkred", "flood": "blue", "landslide": "beige", "glof": "lightblue", "heat": "orange",
                "tsunami": "darkblue", "avalanche": "lightgray", "snow": "white", "cyclone": "purple", "smog": "gray", "drought": "lightred"}

# Approximate representative points for climatic zones
CLIMATE_ZONES = {
    "Polar": ([(35.9, 76.5), (36.3, 75.0), (35.2, 74.6)], "#4a90e2"),
    "Highland": ([(35.8, 71.8), (30.2, 67.0), (34.9, 73.6), (35.9, 74.3)], "#7b8d8e"),
    "Temperate": ([(34.8, 72.4), (33.9, 73.4), (33.7, 73.1), (34.4, 73.5)], "#2ecc71"),
    "Tropical": ([(31.5, 74.3), (30.2, 71.5), (24.9, 67.0), (25.4, 68.4)], "#e67e22"),
    "Arid": ([(24.7, 70.2), (28.9, 72.0), (31.3, 71.5), (28.6, 65.4), (29.0, 64.0)], "#c0392b"),
}

LINK_CANAL_LINES = {
    "Upper Chenab Canal": ("Marala Headworks", "Balloki Headworks"),
    "Upper Jhelum Canal": ("Rasul Barrage", "Khanki Headworks"),
    "Rasul-Qadirabad Link": ("Rasul Barrage", "Qadirabad Barrage"),
    "Qadirabad-Balloki Link": ("Qadirabad Barrage", "Balloki Headworks"),
    "Balloki-Sulemanki Link": ("Balloki Headworks", "Sulemanki Headworks"),
    "Chashma-Jhelum Link": ("Chashma Barrage", "Trimmu Barrage"),
    "Taunsa-Panjnad Link": ("Taunsa Barrage", "Panjnad Headworks"),
    "Trimmu-Sidhnai Link": ("Trimmu Barrage", "Sidhnai Barrage"),
    "Sidhnai-Mailsi-Bahawal Link": ("Sidhnai Barrage", "Islam Headworks"),
}

RISK_POINTS = {  # for hydraulic & risk model map: name -> (lat, lon, base risk 0-1)
    "Tarbela": (34.09, 72.70, 0.4), "Mangla": (33.14, 73.64, 0.35), "Marala": (32.67, 74.46, 0.6),
    "Taunsa": (30.51, 70.85, 0.55), "Guddu": (28.42, 69.71, 0.65), "Sukkur": (27.68, 68.85, 0.7),
    "Kotri": (25.37, 68.31, 0.6), "Nullah Lai (Rawalpindi)": (33.62, 73.06, 0.75), "Swat (Mingora)": (34.77, 72.36, 0.7),
    "Lahore": (31.55, 74.34, 0.5), "Karachi": (24.86, 67.01, 0.65), "Hunza": (36.32, 74.86, 0.8),
}


def _base(zoom=5, center=(30.4, 69.3)):
    return folium.Map(location=list(center), zoom_start=zoom, tiles="OpenStreetMap")


def _rivers(m):
    for r, pts in RIVER_PATHS.items():
        folium.PolyLine(pts, color="#1f77b4", weight=2, opacity=0.6, tooltip=r).add_to(m)


def geopolitical_map():
    m = _base(); _rivers(m)
    for n, (la, lo, c, note) in GEOPOLITICAL.items():
        folium.Marker([la, lo], tooltip=n, popup=note, icon=folium.Icon(color=c)).add_to(m)
    folium.PolyLine([(36.9, 75.4), (35.5, 73.7), (34.0, 73.2), (24.9, 67.0)], color="purple", dash_array="6",
                    tooltip="CPEC corridor (schematic)").add_to(m)
    folium.PolyLine([(24.9, 67.0), (25.1, 62.3)], color="blue", dash_array="4", tooltip="Coastal highway / maritime").add_to(m)
    return m


def china_hydro_map():
    m = _base(7, (34.3, 73.6)); _rivers(m)
    for n, (la, lo, s) in CHINA_HYDRO.items():
        folium.Marker([la, lo], tooltip=n, popup=s, icon=folium.Icon(color="red", icon="flash")).add_to(m)
    return m


def india_projects_map():
    m = _base(7, (33.6, 75.0)); _rivers(m)
    for n, (la, lo, s) in INDIA_PROJECTS.items():
        color = "green" if "Pakistan" in n else "darkred"
        folium.Marker([la, lo], tooltip=n, popup=s, icon=folium.Icon(color=color, icon="warning-sign")).add_to(m)
    return m


def historical_events_map():
    m = _base()
    for n, (la, lo, kind, note) in HISTORICAL_EVENTS.items():
        folium.Marker([la, lo], tooltip=n, popup=f"{kind.title()}: {note}",
                      icon=folium.Icon(color=EVENT_COLORS[kind], icon="exclamation-sign")).add_to(m)
    return m


def climate_map():
    m = _base()
    for zone, (pts, col) in CLIMATE_ZONES.items():
        for la, lo in pts:
            folium.Circle([la, lo], radius=90000, color=col, fill=True, fill_opacity=0.35, tooltip=zone).add_to(m)
    return m


def link_canals_map():
    m = _base(6, (31.2, 72.5)); _rivers(m)
    for n, (a, b) in LINK_CANAL_LINES.items():
        folium.PolyLine([BARRAGES[a], BARRAGES[b]], color="#16a085", weight=4, dash_array="8", tooltip=n).add_to(m)
    for n, (la, lo) in BARRAGES.items():
        folium.CircleMarker([la, lo], radius=5, color="black", fill=True, tooltip=n).add_to(m)
    return m


def risk_map(rain_mm_hr=20, flow_factor=1.0):
    """Risk scaled by rainfall & flow: colour green->red."""
    m = _base()
    scale = min(1.5, rain_mm_hr / 40 + flow_factor * 0.5)
    for n, (la, lo, base) in RISK_POINTS.items():
        r = min(1.0, base * scale)
        col = "green" if r < 0.4 else "orange" if r < 0.7 else "red"
        folium.CircleMarker([la, lo], radius=6 + r * 14, color=col, fill=True, fill_opacity=0.6,
                            tooltip=f"{n}: risk {r:.2f}").add_to(m)
    return m


def _schematic(nodes, edges, title):
    fig = go.Figure()
    for a, b, label, color in edges:
        (x0, y0), (x1, y1) = nodes[a], nodes[b]
        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode="lines", line=dict(color=color, width=3),
                                 hoverinfo="text", text=label, showlegend=False))
    fig.add_trace(go.Scatter(x=[v[0] for v in nodes.values()], y=[v[1] for v in nodes.values()], mode="markers+text",
                             text=list(nodes), textposition="middle right", marker=dict(size=12, color="#333"), showlegend=False))
    fig.update_layout(title=title, height=650, xaxis=dict(visible=False, range=[min(v[0] for v in nodes.values()) - 0.5, max(v[0] for v in nodes.values()) + 3]), yaxis=dict(visible=False), plot_bgcolor="white")
    return fig


def irrigation_hydropower_schematic():
    nodes = {"Tarbela (4,888 MW)": (3, 9), "Ghazi Barotha (1,450 MW)": (3, 8.3), "Mangla (1,000 MW)": (6, 9),
             "Karot (720 MW)": (6.4, 9.6), "Chashma (CHASNUPP/HPP)": (3, 7), "Jinnah": (3, 7.6),
             "Rasul": (6, 8), "Trimmu": (5.5, 6), "Taunsa": (3, 5.5), "Panjnad": (5, 4.3),
             "Guddu": (3, 3.5), "Sukkur": (3, 2.5), "Kotri": (3, 1.2), "Canal commands (Sindh)": (1.3, 2.2),
             "Canal commands (Punjab)": (7.5, 6.8)}
    e = [("Tarbela (4,888 MW)", "Ghazi Barotha (1,450 MW)", "Indus", "#1f4e79"), ("Ghazi Barotha (1,450 MW)", "Jinnah", "Indus", "#1f4e79"),
         ("Jinnah", "Chashma (CHASNUPP/HPP)", "Indus", "#1f4e79"), ("Chashma (CHASNUPP/HPP)", "Taunsa", "Indus", "#1f4e79"),
         ("Taunsa", "Guddu", "Indus", "#1f4e79"), ("Guddu", "Sukkur", "Indus", "#1f4e79"), ("Sukkur", "Kotri", "Indus", "#1f4e79"),
         ("Karot (720 MW)", "Mangla (1,000 MW)", "Jhelum", "#e76f51"), ("Mangla (1,000 MW)", "Rasul", "Jhelum", "#e76f51"),
         ("Rasul", "Trimmu", "Jhelum", "#e76f51"), ("Trimmu", "Panjnad", "Chenab", "#f4a261"), ("Panjnad", "Guddu", "Panjnad", "#264653"),
         ("Chashma (CHASNUPP/HPP)", "Rasul", "C-J Link", "#16a085"), ("Taunsa", "Panjnad", "T-P Link", "#16a085"),
         ("Sukkur", "Canal commands (Sindh)", "Rohri/Nara/Dadu canals", "#8e44ad"), ("Rasul", "Canal commands (Punjab)", "Lower Jhelum/LCC", "#8e44ad")]
    return _schematic(nodes, e, "Irrigation & hydropower network (schematic)")


def confluence_schematic():
    nodes = {"Hunza": (5, 10), "Gilgit": (4, 9.5), "Shyok": (7, 10), "Indus (upper)": (6, 9), "Jaglot": (5, 8.5),
             "Swat": (1.5, 8), "Kabul": (1, 7.5), "Charsadda": (2, 7.2), "Attock": (4, 7), "Jhelum": (8, 7.5),
             "Chenab": (9, 7), "Trimmu": (8, 5.5), "Ravi": (10, 6), "Ahmadpur Sial": (8.5, 4.8), "Sutlej": (10.5, 4.5),
             "Panjnad": (8, 3.5), "Mithankot": (5, 2.5), "Arabian Sea": (4, 0.5)}
    c = "#1f4e79"
    e = [("Hunza", "Gilgit", "Hunza->Gilgit", c), ("Gilgit", "Jaglot", "Gilgit->Indus", c), ("Shyok", "Indus (upper)", "Shyok->Indus", c),
         ("Indus (upper)", "Jaglot", "Indus", c), ("Jaglot", "Attock", "Indus", c), ("Swat", "Charsadda", "Swat->Kabul", "#2a9d8f"),
         ("Kabul", "Charsadda", "Kabul", "#2a9d8f"), ("Charsadda", "Attock", "Kabul->Indus", "#2a9d8f"),
         ("Jhelum", "Trimmu", "Jhelum->Chenab", "#e76f51"), ("Chenab", "Trimmu", "Chenab", "#f4a261"),
         ("Trimmu", "Ahmadpur Sial", "Chenab", "#f4a261"), ("Ravi", "Ahmadpur Sial", "Ravi->Chenab", "#8ab17d"),
         ("Ahmadpur Sial", "Panjnad", "Chenab", "#f4a261"), ("Sutlej", "Panjnad", "Sutlej->Chenab", "#e9c46a"),
         ("Panjnad", "Mithankot", "Panjnad->Indus", "#264653"), ("Attock", "Mithankot", "Indus", c), ("Mithankot", "Arabian Sea", "Indus", c)]
    return _schematic(nodes, e, "River confluence network (schematic)")

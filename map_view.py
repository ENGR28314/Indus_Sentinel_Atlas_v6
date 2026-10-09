"""Interactive Folium map of provinces, rivers, dams, barrages, confluences, lakes, peaks."""
import folium
from coordinates import PROVINCES, DAMS, BARRAGES, CONFLUENCES, LAKES, PEAKS, RIVER_PATHS

LAYERS = {
    "Dams / Hydropower": (DAMS, "red", "tint"),
    "Barrages / Headworks": (BARRAGES, "orange", "road"),
    "Confluences": (CONFLUENCES, "purple", "random"),
    "Lakes": (LAKES, "blue", "info-sign"),
    "Peaks": (PEAKS, "darkgreen", "flag"),
}


def build_map(selected_layers=None, show_rivers=True):
    m = folium.Map(location=[30.4, 69.3], zoom_start=5, tiles="OpenStreetMap")
    folium.TileLayer("cartodbpositron", name="Light").add_to(m)
    for name, (la, lo) in PROVINCES.items():
        folium.CircleMarker([la, lo], radius=8, color="black", fill=True, fill_opacity=0.6,
                            tooltip=name).add_to(m)
    if show_rivers:
        fg = folium.FeatureGroup(name="Rivers")
        for r, pts in RIVER_PATHS.items():
            folium.PolyLine(pts, color="#1f77b4", weight=3, tooltip=r).add_to(fg)
        fg.add_to(m)
    for layer, (pts, color, icon) in LAYERS.items():
        if selected_layers and layer not in selected_layers:
            continue
        fg = folium.FeatureGroup(name=layer)
        for n, (la, lo) in pts.items():
            folium.Marker([la, lo], tooltip=n, icon=folium.Icon(color=color, icon=icon)).add_to(fg)
        fg.add_to(m)
    folium.LayerControl().add_to(m)
    return m

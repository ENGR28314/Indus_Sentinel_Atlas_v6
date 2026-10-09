"""Crop seasons, apiculture, aquaculture and editable input-driven socio/agro data."""
import pandas as pd
import plotly.express as px

RABI = pd.DataFrame([
    ["Rabi", "Wheat", "Nov - Apr", "Highest canal demand Dec-Feb; 4-6 irrigations; Tarbela/Mangla drawdown supports sowing"],
    ["Rabi", "Gram (chickpea)", "Oct - Mar", "Mostly rain-fed (Thal); 1-2 irrigations"],
    ["Rabi", "Mustard / Rapeseed", "Oct - Mar", "Low water need; suits shortage years"],
    ["Rabi", "Barley", "Nov - Apr", "Tolerates saline/marginal water"],
], columns=["season", "crop", "typical_window", "engineering_water_note"])

KHARIF = pd.DataFrame([
    ["Kharif", "Rice", "Jun - Oct", "Very high water (1,200-1,600 mm); depends on Chenab flows at Marala"],
    ["Kharif", "Cotton", "Apr/May - Oct", "Early kharif shortage (Apr-May) critical before monsoon"],
    ["Kharif", "Sugarcane", "Feb/Sep - Dec (annual)", "Year-round demand ~1,500-2,500 mm"],
    ["Kharif", "Maize", "Jul - Oct", "Moderate demand; flood-sensitive"],
], columns=["season", "crop", "typical_window", "engineering_water_note"])

APICULTURE = pd.DataFrame([
    ["Honey production", "tonnes/yr", "National output ~ 7,500-12,000 t (Beri, Phulai, Acacia, citrus honey)"],
    ["Bee colonies", "number", "Managed Apis mellifera colonies, mainly KPK & Punjab"],
    ["Beekeepers", "persons", "Rural households engaged in migratory beekeeping"],
    ["Yield per colony", "kg/colony/yr", "Typical 15-25 kg"],
], columns=["indicator", "unit", "description"])

AQUACULTURE = pd.DataFrame([
    ["Aquaculture production", "tonnes/yr", "Farmed fish (rohu, mori, thaila, tilapia, shrimp)"],
    ["Pond area", "ha", "Inland fish farms, mainly Punjab & Sindh"],
    ["Fish seed hatcheries", "number", "Public & private hatcheries"],
    ["Employment", "persons", "Fish farming & processing workforce"],
], columns=["indicator", "unit", "description"])

DEFAULT_INPUT = pd.DataFrame([
    ["Punjab", 12_500_000, 60_000_000, 9_500_000, 4_000, 120_000],
    ["Sindh", 5_400_000, 22_000_000, 3_800_000, 900, 60_000],
    ["KPK", 1_800_000, 5_500_000, 1_700_000, 3_500, 8_000],
    ["Balochistan", 1_900_000, 3_800_000, 900_000, 400, 3_000],
    ["Gilgit-Baltistan", 60_000, 300_000, 150_000, 100, 500],
    ["AJK", 160_000, 450_000, 200_000, 300, 700],
    ["ICT", 30_000, 70_000, 20_000, 50, 100],
], columns=["province/region", "cultivated area", "crop production", "employment", "honey production", "aquaculture production"])

METRICS = {
    "Cultivated area (ha)": "cultivated area",
    "Crop production (tonnes)": "crop production",
    "Employment (persons)": "employment",
    "Honey production (tonnes)": "honey production",
    "Aquaculture production (tonnes)": "aquaculture production",
}
GRAPH_TYPES = ["Bar chart", "Pie chart", "Scatter plot", "Line chart"]


def make_chart(df, graph, metric_label):
    col, x = METRICS[metric_label], "province/region"
    if graph == "Bar chart":
        return px.bar(df, x=x, y=col, title=metric_label)
    if graph == "Pie chart":
        return px.pie(df, names=x, values=col, title=metric_label)
    if graph == "Scatter plot":
        return px.scatter(df, x="cultivated area", y=col, text=x, size=col, title=f"{metric_label} vs cultivated area")
    return px.line(df, x=x, y=col, markers=True, title=metric_label)

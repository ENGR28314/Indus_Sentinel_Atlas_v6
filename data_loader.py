"""Core reference data: provinces, rivers, infrastructure, climate, mountains, lakes."""
import pandas as pd
from coordinates import DAMS, BARRAGES, CONFLUENCES, LAKES, PEAKS

PROVINCES = {
    "Gilgit-Baltistan": {
        "capital": "Gilgit", "climate": "Polar / Highland / Temperate",
        "rivers": ["Indus", "Gilgit", "Hunza", "Shyok", "Shigar", "Astore"],
        "dams": ["Diamer-Bhasha Dam (u/c)", "Satpara Dam"],
        "ranges": ["Karakoram", "Himalayas", "Hindu Kush", "Hindu Raj"],
        "notes": "Over 7,000 glaciers; highest GLOF exposure; Karakoram Highway lifeline.",
    },
    "Khyber Pakhtunkhwa (KPK)": {
        "capital": "Peshawar", "climate": "Temperate (north) / Arid-semi-arid (south)",
        "rivers": ["Indus", "Kabul", "Swat", "Panjkora", "Kunhar", "Chitral", "Kurram", "Gomal"],
        "dams": ["Tarbela Dam", "Warsak Dam", "Mohmand Dam (u/c)", "Gomal Zam Dam", "Dasu Dam (u/c)"],
        "ranges": ["Hindu Kush", "Hindu Raj", "Spin Ghar", "Himalayas (Kaghan)"],
        "notes": "Flash floods in Swat/Chitral; 2005 earthquake zone; Peshawar valley agriculture.",
    },
    "Punjab": {
        "capital": "Lahore", "climate": "Tropical / Arid (south) / Semi-arid",
        "rivers": ["Indus", "Jhelum", "Chenab", "Ravi", "Sutlej", "Beas (seasonal)"],
        "dams": ["Mangla (shared AJK)", "Rawal", "Simly (ICT)"],
        "ranges": ["Salt Range", "Sulaiman (DG Khan)"],
        "notes": "Breadbasket; dense link canal network; riverine & urban flooding (Lahore).",
    },
    "Sindh": {
        "capital": "Karachi", "climate": "Arid / Tropical (coastal)",
        "rivers": ["Indus"],
        "dams": ["Hub Dam (shared)"],
        "ranges": ["Kirthar Range"],
        "notes": "Lower riparian; Indus Delta degradation, sea intrusion, heatwaves, 2022 floods.",
    },
    "Balochistan": {
        "capital": "Quetta", "climate": "Arid / Highland",
        "rivers": ["Hingol", "Hub", "Porali", "Dasht", "Zhob", "Nari", "Bolan"],
        "dams": ["Mirani Dam", "Hub Dam", "Sabakzai Dam"],
        "ranges": ["Sulaiman", "Toba Kakar", "Kirthar", "Central Brahui", "Makran Coast"],
        "notes": "Chronic drought, water stress, Makran subduction tsunami risk, Gwadar port.",
    },
    "Azad Jammu and Kashmir": {
        "capital": "Muzaffarabad", "climate": "Temperate / Highland",
        "rivers": ["Jhelum", "Neelum", "Poonch", "Kunhar (confluence)"],
        "dams": ["Mangla Dam", "Neelum-Jhelum HPP", "Karot HPP", "Kohala HPP (planned)", "Azad Pattan HPP (planned)"],
        "ranges": ["Pir Panjal (Himalayas)"],
        "notes": "2005 Kashmir earthquake epicentre; CPEC hydropower cluster on Jhelum.",
    },
    "Islamabad Capital Territory (ICT)": {
        "capital": "Islamabad", "climate": "Humid subtropical",
        "rivers": ["Korang", "Soan"],
        "dams": ["Rawal Dam", "Simly Dam", "Khanpur (nearby)"],
        "ranges": ["Margalla Hills (Himalayan foothills)"],
        "notes": "Cloudbursts & urban flooding (Nullah Lai), seismic zone near Margalla fault.",
    },
}

RIVERS = pd.DataFrame([
    ["Indus", "Tibet (Lake Mansarovar area)", "Arabian Sea (Keti Bandar)", 3180, "Tarbela, Jinnah, Chashma, Taunsa, Guddu, Sukkur, Kotri", "Gilgit, Kabul, Panjnad"],
    ["Jhelum", "Verinag spring (IIOJK)", "Chenab at Trimmu", 725, "Mangla, Rasul", "Neelum, Kunhar, Poonch"],
    ["Chenab", "Himachal Pradesh (Chandra-Bhaga)", "Panjnad", 960, "Marala, Khanki, Qadirabad, Trimmu, Panjnad", "Jhelum, Ravi, Sutlej"],
    ["Ravi", "Kangra, Himachal Pradesh", "Chenab near Ahmadpur Sial", 720, "Balloki, Sidhnai", "-"],
    ["Sutlej", "Lake Rakshastal (Tibet)", "Chenab at Panjnad", 1450, "Sulemanki, Islam", "Beas (in India)"],
    ["Kabul", "Sanglakh Range (Afghanistan)", "Indus at Attock", 700, "Warsak, Munda (Mohmand)", "Swat, Chitral/Kunar"],
    ["Gilgit", "Shandur Lake", "Indus near Jaglot", 240, "-", "Hunza, Ghizer"],
    ["Swat", "Kalam (Ushu & Gabral)", "Kabul at Charsadda", 240, "Amandara, Munda HW", "Panjkora"],
], columns=["River", "Source (Upstream)", "Mouth (Downstream)", "Length_km", "Major Barrages/Dams", "Tributaries"])

LINK_CANALS = pd.DataFrame([
    ["Upper Chenab Canal (UCC)", "Marala", "Balloki", 21500],
    ["Marala-Ravi Link", "Marala", "Ravi", 22000],
    ["Upper Jhelum Canal", "Mangla", "Khanki", 8500],
    ["Rasul-Qadirabad Link", "Rasul", "Qadirabad", 19000],
    ["Qadirabad-Balloki Link", "Qadirabad", "Balloki", 18600],
    ["Balloki-Sulemanki Link", "Balloki", "Sulemanki", 18500],
    ["Chashma-Jhelum Link", "Chashma", "Jhelum (below Rasul)", 21700],
    ["Taunsa-Panjnad Link", "Taunsa", "Panjnad", 12000],
    ["Trimmu-Sidhnai Link", "Trimmu", "Sidhnai", 11000],
    ["Sidhnai-Mailsi-Bahawal Link", "Sidhnai", "Bahawal", 10100],
], columns=["Link Canal", "Off-take", "Outfall", "Capacity_cusecs"])

DAMS_TABLE = pd.DataFrame([
    ["Tarbela", "Indus", "KPK", 1976, 13.69, 4888, "Earth & rock fill"],
    ["Mangla", "Jhelum", "AJK", 1967, 7.39, 1000, "Earth fill (raised 2009)"],
    ["Warsak", "Kabul", "KPK", 1960, 0.03, 243, "Concrete gravity"],
    ["Khanpur", "Haro", "KPK", 1983, 0.09, 0, "Rock fill"],
    ["Hub", "Hub", "Sindh/Balochistan", 1981, 0.86, 0, "Earth fill"],
    ["Mirani", "Dasht", "Balochistan", 2006, 0.30, 0, "Earth core rock fill"],
    ["Gomal Zam", "Gomal", "KPK", 2013, 0.89, 17, "RCC gravity"],
    ["Diamer-Bhasha (u/c)", "Indus", "GB/KPK", 2029, 8.10, 4500, "RCC gravity, 272 m"],
    ["Mohmand (u/c)", "Swat", "KPK", 2027, 0.68, 800, "CFRD, 213 m"],
    ["Dasu (u/c)", "Indus", "KPK", 2027, 1.15, 4320, "RCC run-of-river"],
], columns=["Dam", "River", "Province", "Year", "Gross_Storage_MAF", "Power_MW", "Type"])

CLIMATE_REGIONS = pd.DataFrame([
    ["Polar", "GB high Karakoram, upper Himalaya", "Below 0 °C most of year; permanent snow/glaciers", "Avalanches, GLOFs"],
    ["Highland", "GB, Chitral, Kaghan, Quetta plateau", "Cold winters, mild summers; snowfall", "Landslides, snow contingencies"],
    ["Temperate", "Swat, Murree, AJK, Islamabad", "Moderate; monsoon & western disturbances", "Flash floods, cloudbursts"],
    ["Tropical", "Central/South Punjab, Sindh coast", "Hot summers 40-50 °C; humid monsoon", "Heatwaves, riverine floods, cyclones"],
    ["Arid", "Thar, Cholistan, Thal, Kharan, Chagai", "Rain < 250 mm/yr; extreme diurnal range", "Drought, water stress, dust storms"],
], columns=["Climatic Region", "Areas", "Characteristics", "Dominant Hazards"])

MOUNTAINS = {
    "1. Northern Highlands and Major Ranges": {
        "Karakoram Range": dict(peak="K2 (8,611 m)", other="Gasherbrum I & II, Broad Peak, Masherbrum, Rakaposhi",
            surroundings="Skardu, Hunza, Shigar, Baltoro & Siachen glaciers", rivers="Indus, Shyok, Hunza, Shigar",
            climbing="Base: Askole->Concordia (8-10 day trek). Season Jun-Aug. Permits from Alpine Club/GB Tourism; liaison officer mandatory. Abruzzi Spur standard route; Bottleneck serac hazard.",
            geology="Collision of Kohistan-Ladakh arc with Karakoram plate (Main Karakoram Thrust); granite batholiths, metamorphic gneiss; actively uplifting.",
            guide="Fly Islamabad-Skardu; visit Shigar Fort, Deosai, Shangrila; Hunza valley via KKH; Khunjerab Pass (4,693 m)."),
        "Himalayas Range": dict(peak="Nanga Parbat (8,126 m)", other="Rakhiot Peak, Malika Parbat (Kaghan)",
            surroundings="Astore, Fairy Meadows, Kaghan, Neelum, AJK", rivers="Indus, Jhelum, Neelum, Kunhar, Astore",
            climbing="'Killer Mountain'. Kinshofer route (Diamir face) common; Rupal face is world's highest wall (~4,600 m). Season Jun-Jul. Fairy Meadows base via Raikot Bridge.",
            geology="Western syntaxis of Himalaya; Nanga Parbat-Haramosh massif exhumed rapidly; MMT & MBT faults; high seismicity.",
            guide="Fairy Meadows jeep+hike; Naran-Kaghan, Babusar Top, Lake Saif-ul-Malook, Neelum Valley (Arang Kel)."),
        "Hindu Kush Range": dict(peak="Tirich Mir (7,708 m)", other="Noshaq (7,492 m), Istor-o-Nal",
            surroundings="Chitral, Kalash valleys, Wakhan border", rivers="Chitral (Kunar), Mastuj, Kabul tributaries",
            climbing="Approach via Chitral-Barum glacier; south face/ SW ridge routes. Season Jul-Aug; NOC needed for border zones.",
            geology="Hindu Kush deep-focus seismic zone (up to 250 km depth); sedimentary & metamorphic rocks.",
            guide="Chitral Fort, Kalash Valleys (Bumburet), Shandur Polo festival, Garam Chashma hot springs."),
        "Hindu Raj Range": dict(peak="Koyo Zom (6,872 m)", other="Buni Zom, Thui peaks",
            surroundings="Yasin, Ghizer, Ishkoman, upper Swat", rivers="Gilgit, Ghizer, Yasin, Swat (headwaters)",
            climbing="Remote alpine climbs; Thui Pass trek (4,500 m). Season Jul-Sep.",
            geology="Kohistan island-arc terrane; volcanic & plutonic rocks.",
            guide="Phander Lake, Ghizer valley, Shandur Pass, Mahodand Lake (Kalam)."),
    },
    "2. Western and Southern Border Ranges": {
        "Spin Ghar (Koh-e-Safed)": dict(peak="Sikaram (4,755 m)", other="-", surroundings="Kurram, Khyber, Parachinar",
            rivers="Kurram, Bara", climbing="Border zone; restricted access, security NOC required.",
            geology="Folded sedimentary limestones; Afghan-Indian plate boundary.", guide="Parachinar valley, Khyber Pass, Torkham."),
        "Sulaiman Mountains (Koh-e-Suleman)": dict(peak="Takht-e-Sulaiman (3,487 m)", other="Fort Munro (1,800 m)",
            surroundings="DG Khan, Zhob, Musakhel, Waziristan", rivers="Gomal, Zhob, hill torrents (Vehowa, Sanghar)",
            climbing="Day hikes at Fort Munro; Takht ascent via Zhob/Darazinda with local guides.",
            geology="Sulaiman fold-thrust belt; limestone/shale; hydrocarbons (Sui, Dera Bugti).",
            guide="Fort Munro hill station, Zhob valley, Kingri caves."),
        "Kirthar Range": dict(peak="Zardak / Kutte-jo-Kabar (~2,260 m)", other="Gorakh Hill (1,734 m)",
            surroundings="Dadu, Jamshoro, Khuzdar; Kirthar National Park", rivers="Hub, Gaj, Nari hill torrents",
            climbing="Gorakh Hill road access; trekking Nov-Feb.", geology="Tertiary limestone fold belt; Ornach-Nal fault.",
            guide="Gorakh Hill, Kirthar NP (ibex, urial), Ranikot Fort."),
        "Toba Kakar Range": dict(peak="Zarghun Ghar area (~3,578 m)", other="Khwaja Amran",
            surroundings="Quetta, Pishin, Killa Saifullah, Ziarat", rivers="Pishin Lora, Zhob, Kadanai",
            climbing="Hikes in Ziarat juniper forests; Khojak Pass.", geology="Chaman transform fault (active, strike-slip).",
            guide="Ziarat Residency, Hanna Lake, Urak valley."),
        "Salt Range": dict(peak="Sakesar (1,522 m)", other="Tilla Jogian (975 m)",
            surroundings="Jhelum, Chakwal, Khushab, Mianwali", rivers="Jhelum, Soan (north)",
            climbing="Easy hikes; Tilla Jogian, Katas Raj, Kallar Kahar.", geology="Precambrian-Eocene exposed sequence ('geological museum'); Salt Range Thrust; rock salt.",
            guide="Khewra Salt Mine, Katas Raj temples, Kallar Kahar & Uchhali lakes."),
    },
}

LAKES_TABLE = pd.DataFrame([
    ["Saif-ul-Malook", "KPK", "Glacial/alpine"], ["Mahodand", "KPK", "Alpine"], ["Lulusar", "KPK", "Alpine"],
    ["Ansoo", "KPK", "Alpine"], ["Attabad", "GB", "Landslide-dammed (2010)"], ["Satpara", "GB", "Glacial/dam"],
    ["Sheosar", "GB", "Alpine (Deosai)"], ["Kachura (Upper/Lower)", "GB", "Alpine"], ["Rama", "GB", "Glacial"],
    ["Borith", "GB", "Brackish"], ["Karambar", "GB", "High-altitude"], ["Rush Lake", "GB", "High-altitude (4,694 m)"],
    ["Kalar Kahar", "Punjab", "Salt Range"], ["Uchhali", "Punjab", "Saline (Ramsar)"], ["Namal", "Punjab", "Reservoir"],
    ["Keenjhar", "Sindh", "Freshwater (Karachi supply)"], ["Manchar", "Sindh", "Largest freshwater"], ["Haleji", "Sindh", "Bird sanctuary"],
    ["Hamal", "Sindh", "Seasonal"], ["Hanna", "Balochistan", "Reservoir"], ["Zangi Nawar", "Balochistan", "Desert wetland"],
    ["Banjosa", "AJK", "Artificial"], ["Ratti Gali", "AJK", "Glacial"], ["Rawal", "ICT", "Reservoir"],
], columns=["Lake", "Province", "Type"])


def points_df():
    rows = []
    for kind, d in [("Dam/HPP", DAMS), ("Barrage", BARRAGES), ("Confluence", CONFLUENCES), ("Lake", LAKES), ("Peak", PEAKS)]:
        for n, (la, lo) in d.items():
            rows.append(dict(name=n, type=kind, lat=la, lon=lo))
    return pd.DataFrame(rows)


# ---------------- 12-Month Historical Telemetry Engine ----------------
import numpy as np

GAUGES = {"Tarbela (Indus)": (1490, 1550, 30), "Mangla (Jhelum)": (1150, 1242, 25),
          "Marala (Chenab)": (250, 256, 2.5), "Balloki (Ravi)": (185, 190, 2.0)}


def telemetry_12_months(seed=42, end=None):
    """Simulated daily gauge levels (m) for 12 months: peaks Jun-Aug, lows Dec-Jan."""
    rng = np.random.default_rng(seed)
    end = pd.Timestamp(end) if end else pd.Timestamp.today().normalize()
    dates = pd.date_range(end - pd.Timedelta(days=364), end, freq="D")
    season = 0.5 * (1 + np.cos(2 * np.pi * (dates.dayofyear.values - 200) / 365))
    out = {"date": dates}
    for g, (low, high, noise) in GAUGES.items():
        out[g] = np.round(low + (high - low) * season + rng.normal(0, noise * 0.1, len(dates)), 2)
    return pd.DataFrame(out)

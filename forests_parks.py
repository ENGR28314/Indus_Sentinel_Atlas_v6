"""Forest types, notable forests and national/urban parks of Pakistan (approximate data)."""

FOREST_TYPES = {
    "Coniferous Forests": "Northern mountains at 1,000-4,000 m (KPK, Gilgit-Baltistan, AJK, Murree); pine (chir, blue pine), fir, spruce and deodar.",
    "Mangrove Forests": "Coastal wetlands of the Indus Delta (Karachi, Thatta, Keti Bandar) and Balochistan coast (Miani Hor, Jiwani) on the Arabian Sea; mainly Avicennia marina.",
    "Riverain (Bela) Forests": "Narrow strips along the Indus and its tributaries (Sindh & Punjab); kikar (babul), shisham, bahan (poplar), tamarisk.",
    "Tropical Thorn (Scrub) Forests": "Low-lying plains and semi-arid flatlands of Punjab and Sindh; jand, karir, van, beri.",
    "Irrigated/Planted Forests": "Man-made forests such as Changa Manga near Lahore (one of the world's oldest planted forests), Chichawatni, Thal; created to meet timber demand.",
}

# name: (province, lat, lon, area, history, wildlife, attractions)
FORESTS = {
    "Changa Manga Forest": ("Punjab (Kasur)", 31.08, 73.97, "~4,860 ha (12,000 acres)", "Planted by the British in 1866 to supply fuelwood for railways; named after two dacoit brothers.", "Shisham, mulberry; hog deer, jackals, peafowl, many birds.", "Miniature train, lake boating, Changa Manga wildlife park."),
    "Ziarat Juniper Forest": ("Balochistan", 30.38, 67.73, "~110,000 ha", "Among the world's largest & oldest juniper forests; some trees 3,000-5,000 years old. UNESCO biosphere reserve (2013).", "Juniperus excelsa; Suleiman markhor, urial, wolves, chukar.", "Quaid-e-Azam Residency, Prospect Point, Sandeman Tangi."),
    "Ushu Forest": ("KPK (Swat - Kalam)", 35.55, 72.62, "Part of Kalam forests", "Ancient deodar/pine forest along Ushu river above Kalam.", "Deodar, blue pine, fir; snow leopard (rare), black bear, monal.", "Mahodand Lake road, camping, trout fishing."),
    "Dir Forest": ("KPK (Upper/Lower Dir)", 35.20, 71.88, "Extensive coniferous belt", "Traditional timber forests of former Dir state.", "Deodar, blue pine; leopards, markhor.", "Kumrat valley, Jahaz Banda meadows."),
    "Soon Valley Forest": ("Punjab (Khushab)", 32.58, 72.12, "Salt Range scrub/olive", "Ancient Salt Range landscape; wild olive & phulai forest.", "Urial, chinkara; migratory birds at Uchhali.", "Uchhali, Khabeki, Jahlar lakes; Sakesar."),
    "Mukshpuri Forest": ("KPK (Nathia Gali)", 34.07, 73.39, "Part of Ayubia NP", "Galiyat oak-pine forest on Mukshpuri peak (2,800 m).", "Common leopard, yellow-throated marten, monal.", "Mukshpuri & Miranjani hikes, Dunga Gali."),
    "Rama Meadows Forest": ("Gilgit-Baltistan (Astore)", 35.36, 74.81, "Alpine meadow-forest", "Pine forest on the flanks of Nanga Parbat.", "Blue pine, birch; ibex, brown bear.", "Rama Lake, Nanga Parbat views, camping."),
    "Kalam Forest": ("KPK (Swat)", 35.49, 72.58, "~ Swat Kohistan belt", "Dense deodar forests at confluence of Ushu & Gabral rivers.", "Deodar, fir; monal, black bear.", "Ushu forest, Mahodand Lake, Matiltan."),
    "Chitral Forests": ("KPK (Chitral)", 35.85, 71.78, "Holm oak & conifer belts", "Includes Chitral Gol, Kalash valley forests.", "Kashmir markhor, snow leopard.", "Kalash valleys, Chitral Gol NP."),
    "Margalla Hills Scrub Forests": ("ICT", 33.74, 73.05, "~17,386 ha (Margalla Hills NP)", "Himalayan foothill subtropical scrub & chir pine; protected since 1980.", "Barking deer, leopard, porcupine, 250+ bird species.", "Trail 3 & 5, Daman-e-Koh, Pir Sohawa."),
}

# name: (province, lat, lon, area, info)
PARKS = {
    "Ayub National Park": ("Punjab (Rawalpindi)", 33.56, 73.08, "~930 ha", "Urban park with lake, Jungle Kingdom and aquarium."),
    "Jallo Park, Lahore": ("Punjab", 31.57, 74.47, "~182 ha", "Botanical garden, wildlife park, butterfly house."),
    "Lulusar-Dudipatsar National Park": ("KPK (Kaghan)", 35.03, 73.90, "~75,058 ha", "Alpine lakes; snow leopard, black bear, Himalayan ibex."),
    "Lal Suhanra National Park": ("Punjab (Bahawalpur)", 29.38, 71.97, "~51,368 ha", "UNESCO biosphere reserve; desert, forest & Patisar lake; blackbuck."),
    "Kirthar National Park": ("Sindh", 25.75, 67.65, "~308,733 ha", "Sindh ibex, urial, chinkara; Ranikot Fort nearby."),
    "Khunjerab National Park": ("Gilgit-Baltistan", 36.78, 75.40, "~226,913 ha", "Marco Polo sheep, snow leopard; one of the highest parks."),
    "City Park Multan": ("Punjab", 30.20, 71.47, "Urban", "Family recreation park."),
    "Kashmir Park": ("Punjab (Multan)", 30.18, 71.45, "Urban", "Urban recreational park."),
    "DHA Multan Park": ("Punjab", 30.16, 71.55, "Urban", "Residential green park."),
    "Chitral Gol National Park": ("KPK", 35.90, 71.70, "~7,750 ha", "Kashmir markhor stronghold."),
    "Chaman Zar-e-Askari Park, Multan": ("Punjab", 30.19, 71.44, "Urban", "Amusement & recreation park."),
    "Jinnah Park": ("Punjab (Rawalpindi)", 33.59, 73.05, "Urban", "Recreation & commercial park."),
    "Hingol National Park": ("Balochistan", 25.50, 65.50, "~619,043 ha", "Largest NP; Princess of Hope, Hinglaj, mud volcanoes, Ibex."),
    "Shakarparian National Park": ("ICT", 33.69, 73.07, "~20 ha", "Hills with Pakistan Monument, Lok Virsa."),
    "Faisal Park, Mumtazabad": ("Punjab (Multan)", 30.16, 71.49, "Urban", "Neighbourhood park."),
    "Pir Lasura National Park": ("AJK (Kotli)", 33.45, 73.95, "~1,580 ha", "Subtropical pine forest."),
    "Hazarganji-Chiltan National Park": ("Balochistan (Quetta)", 30.10, 66.90, "~32,500 ha", "Chiltan ibex (endemic)."),
    "Pakistan Park": ("Punjab", 31.53, 74.33, "Urban", "Urban park."),
    "Machiara National Park": ("AJK (Muzaffarabad)", 34.52, 73.62, "~13,532 ha", "Western tragopan, musk deer, leopard."),
    "Rajana Forest Bhagat Wildlife Park": ("Punjab (Toba Tek Singh)", 30.88, 72.67, "Plantation", "Wildlife enclosure in irrigated forest."),
    "Margalla Hills National Park": ("ICT", 33.74, 73.05, "~17,386 ha", "Hiking trails, leopards, rich birdlife."),
}

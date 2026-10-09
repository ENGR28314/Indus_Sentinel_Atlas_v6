"""Chenab projects, flow concerns and IWT - content for the 'Indian Atrocities' tab and CoA timeline.
Text reflects Pakistan's stated position as supplied by the project owner."""

CANALS = {
    "1(A). Two new canal systems to be created in India": [
        "The canal linking Chenab with Ravi-Beas-Sutlej would ensure full use of the eastern rivers (Ravi, Beas, Sutlej) and help India use its entire allocated share in the western rivers (Indus, Jhelum, Chenab) under the IWT.",
        "The project is proposed to be completed in three years.",
    ],
    "1(B). Ravi-Beas link and fast-tracked hydropower": [
        "A Ravi-Beas link to tap water flowing beyond treaty limits into Pakistan.",
        "Expediting under-construction projects: Pakal Dul (1,000 MW), Ratle (850 MW), Kiru (624 MW), Kwar (540 MW).",
        "Substantive Limits on Water Control: Pakistan asserts that the designs of Kishanganga and Ratle introduce excessive pondage, giving India structural capacity to manipulate flows.",
        "Enforcement of Interim Measures: Backed by the PCA's 31 Aug 2026 ruling, Pakistan maintains India must comply with court-ordered temporary restrictions on Ratle construction while a parallel technical review proceeds.",
    ],
}

# metric: (icon, definition, dispute, concern)
DISPUTED_SPECS = {
    "Pondage Capacity (Live Storage)": ("🌊", "Volume stored behind a dam to handle daily fluctuations in power demand.",
        "Kishanganga: India 7.5 MCM vs Pakistan's 1 MCM cap. Ratle: India 24 MCM vs Pakistan's 8 MCM.",
        "Excess pondage lets India store water in critical sowing seasons or release sudden surges - man-made droughts or floods downstream."),
    "Orifice Spillways & Gate Placements": ("📐", "Spillways release excess floodwater for dam safety.",
        "India uses deep low-level orifice, gated spillways for silt flushing. Pakistan demands higher/ungated spillways - Ratle spillways raised by 20 m.",
        "Low-level gates allow an upstream state to drain a reservoir in conflict, giving strategic control of river levels."),
    "Intake Submergence Levels": ("🔌", "The intake funnels river water into tunnels to the turbines.",
        "Pakistan asks India to raise power intakes by 1.4 m at Kishanganga and up to 8.8 m at Ratle.",
        "Deep intakes allow generation and drawdown at extreme low levels, maximizing Indian flexibility at the expense of downstream flow consistency."),
    "Freeboard Heights": ("🧗", "Vertical distance between max reservoir level and dam crest - safety buffer.",
        "Ratle: India 2 m freeboard vs Pakistan's 1 m.",
        "Inflated freeboard viewed as a hidden provision to hold more water than declared."),
}

PONDAGE_CHART = [
    {"Project": "Kishanganga", "Party": "India design", "MCM": 7.5}, {"Project": "Kishanganga", "Party": "Pakistan cap", "MCM": 1.0},
    {"Project": "Ratle", "Party": "India design", "MCM": 24.0}, {"Project": "Ratle", "Party": "Pakistan cap", "MCM": 8.0},
]

NEUTRAL_EXPERT_SCHEDULE = [
    ("Nov 2026", "Synthesis Memorandum distributed"),
    ("Feb 2027", "7th Meeting & final hydraulic modelling exercise"),
    ("Mar 2027", "Circulation of the Draft Technical Decision"),
    ("Jul 2027", "Issuance of the Final Legally Binding Determination"),
]

GROUND_REALITY = {
    "The Concrete Freeze": "On 31 Aug 2026 the CoA issued an interim enforcement order prohibiting India from pouring concrete on Ratle's dam wall and power intakes above specified elevations, until 90 days after the Neutral Expert's final decision (effectively to ~Oct 2027).",
    "The Engineering Risk": "If the Neutral Expert rules in Jul 2027 that pondage or spillway designs violate the treaty, India would have to alter designs; modifying poured reinforced concrete would bring major engineering complications and losses.",
    "India's Defiance": "India considers the CoA 'illegally constituted', dismissed the freeze, and its Environment Ministry extended Ratle's environmental clearance through 2030.",
}

COA_TIMELINE_ADDITIONS = [
    "Validity of the Court of Arbitration: Pakistan actively participates in the PCA process and argues the CoA is a legally sound dispute-resolution body properly constituted under Article IX of the IWT.",
    "India proposes inter-basin water transfers: feasibility studies to begin immediately for a 113 km canal redirecting 'surplus' Indus-system flows to Punjab, Haryana and Rajasthan.",
    "31 Aug 2026: CoA interim order freezing Ratle concrete works above specified elevations.",
]


# 17 official Indian Indus-basin hydro projects in J&K
# Source (as supplied by user): CEA "Profile on Hydro Development for U.T. of J&K" (15 Jun 2026); NHPC project pages.
# Coordinates are approximate (schematic placement by district and river).
CEA_PROJECTS = [
    # no, name, river, district, MW, status, lat, lon
    (1, "Uri-I", "Jhelum", "Baramulla", 480, "Operational", 34.08, 74.05),
    (2, "Uri-II", "Jhelum", "Baramulla", 240, "Operational", 34.10, 74.12),
    (3, "Lower Jhelum", "Jhelum", "Baramulla", 105, "Operational", 34.19, 74.37),
    (4, "Upper Sindh-II & Ext.", "Sindh Nallah", "Ganderbal", 105, "Operational", 34.28, 74.85),
    (5, "Kishanganga", "Kishanganga", "Bandipora", 330, "Operational", 34.65, 74.75),
    (6, "Dulhasti", "Chenab", "Kishtwar", 390, "Operational", 33.36, 75.80),
    (7, "Salal I & II", "Chenab", "Reasi/Udhampur", 690, "Operational", 33.15, 74.81),
    (8, "Baglihar-I", "Chenab", "Ramban", 450, "Operational", 33.18, 75.33),
    (9, "Baglihar-II", "Chenab", "Ramban", 450, "Operational", 33.16, 75.31),
    (10, "Sewa-II", "Sewa", "Kathua", 120, "Operational", 32.62, 75.75),
    (11, "Pakal Dul", "Marusudar", "Kishtwar", 1000, "Under construction", 33.45, 75.82),
    (12, "Parnai", "Suran", "Poonch", 37.5, "Under construction", 33.73, 74.28),
    (13, "Kiru", "Chenab", "Kishtwar", 624, "Under construction", 33.38, 75.88),
    (14, "Ratle", "Chenab", "Kishtwar", 850, "Under construction", 33.32, 75.75),
    (15, "Kwar", "Chenab", "Kishtwar", 540, "Under construction", 33.40, 75.85),
    (16, "Uri-I Stage-II", "Jhelum", "Baramulla", 240, "Under construction", 34.09, 74.08),
    (17, "Dulhasti Stage-II", "Chenab", "Kishtwar", 260, "Under construction", 33.37, 75.79),
]
CEA_NOTE = "Separate CEA-concurred projects not counted in this 17 include Sawalkote and Kirthai-II."

CEA_CHANNELS = {
    "Uri-I": "Jhelum River", "Uri-II": "Jhelum River", "Lower Jhelum": "Jhelum River",
    "Upper Sindh-II & Ext.": "Sindh River (Jhelum tributary)", "Kishanganga": "Kishanganga River (Jhelum tributary)",
    "Dulhasti": "Chenab River", "Salal I & II": "Chenab River", "Baglihar-I": "Chenab River", "Baglihar-II": "Chenab River",
    "Sewa-II": "Sewa River (Ravi/Chenab basin)", "Pakal Dul": "Marusudar River (Chenab storage scheme)",
    "Parnai": "Parnai River (Jhelum tributary)", "Kiru": "Chenab River", "Ratle": "Chenab River", "Kwar": "Chenab River",
    "Uri-I Stage-II": "Jhelum River", "Dulhasti Stage-II": "Chenab River",
}
CEA_DESC_OPERATIONAL = [
    "Uri-I & Uri-II on the Jhelum River system", "Lower Jhelum on the Jhelum River",
    "Upper Sindh-II & Extension on the Sindh River (tributary of Jhelum)", "Kishenganga on the Kishanganga River (tributary of Jhelum)",
    "Dulhasti on the Chenab River", "Salal I & II on the Chenab River", "Baglihar-I & Baglihar-II on the Chenab River",
    "Sewa-II on the Sewa River (tributary of Ravi/Chenab basin)",
]
CEA_DESC_UC = [
    "Pakal Dul on the Marusudar River (tributary of Chenab)", "Parnai on the Parnai River (tributary of Jhelum)",
    "Kiru on the Chenab River", "Ratle on the Chenab River", "Kwar on the Chenab River",
    "Uri-I Stage-II on the Jhelum River", "Dulhasti Stage-II on the Chenab River",
]

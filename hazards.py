"""National Disaster Risk Context: hazard profile, vulnerability, emerging risks, scenarios."""

HAZARD_PROFILE = {
    "(A) Hydro-meteorological Hazards": {
        "(1) Floods": {
            "(a) Riverine Floods": "Indus and eastern tributaries overflow during monsoon (Jul-Sep); 2010 & 2022 super floods affected 20M and 33M people.",
            "(b) Flash Floods / Hill Torrents": "Sudden runoff in Swat, Chitral, DG Khan (Koh-e-Suleman torrents), Balochistan nullahs.",
            "(c) Urban Flooding": "Karachi, Lahore, Rawalpindi (Nullah Lai) - choked drains, encroached natural channels.",
            "(d) Mudflows": "Debris-laden flows in GB/KPK valleys after intense rain or glacier surges.",
            "(e) Cloudbursts": ">100 mm/hr localized rain - Islamabad 2001 (620 mm in 10 hrs), Swat, Murree, AJK.",
        },
        "(2) Monsoon Variability": "Early onset, extended seasons and 'short burst' rainfall distribution.",
        "(3) Droughts": "Thar, Cholistan, Balochistan (1998-2002 drought); groundwater depletion.",
        "(4) GLOFs": "3,000+ glacial lakes in GB/KP; ~33 classified hazardous (UNDP GLOF-II).",
        "(5) Heatwaves": "Karachi 2015 (1,200+ deaths); Jacobabad among hottest cities (>50 °C).",
        "(6) Water Stress": "Per-capita availability < 1,000 m3 - water-scarce threshold; storage only ~30 days.",
    },
    "(B) Pakistan's Tectonic Setting": {
        "(1) Earthquakes": "Indian-Eurasian collision; 2005 Kashmir M7.6 (86,000 deaths), 2013 Awaran M7.7.",
        "(2) Landslides": "KKH, Neelum, Hunza; Attabad 2010 dammed the Hunza River.",
        "(3) Avalanches": "Gayari 2012 (Siachen) buried 140; Chitral, Neelum frequent.",
        "(4) Tsunamis": "Makran Subduction Zone - 1945 M8.1 tsunami hit Pasni/Ormara/Karachi.",
        "(5) Seismic Activity and Land Shifts": "Chaman, Main Boundary Thrust, Salt Range Thrust; subsidence in Quetta (~10 cm/yr).",
        "(6) Snow Contingencies": "Murree 2022 snowstorm tragedy; Babusar, Lowari closures.",
    },
    "(C) Climatological & Emerging Hazards": {
        "(1) Accelerated Glacier Melt": "Hindu Kush-Himalaya glaciers losing mass; Karakoram anomaly weakening.",
        "(2) Sea-Level Rise and Cyclones": "Cyclones Yemyin 2007, Biparjoy 2023; delta retreat.",
        "(3) Smog": "Punjab Oct-Jan: crop burning + vehicular/industrial emissions; AQI > 500 in Lahore.",
        "(4) Pollution (Air, Water, Soil)": "Arsenic in groundwater, untreated effluents in Ravi, pesticide residues.",
        "(5) Unpredictably Erratic Global Climate Patterns": "El Nino/La Nina swings, compound events.",
    },
    "(D) Anthropogenic Hazards": {
        "(1) Industrial Accidents and Chemical Spills": "Baldia factory fire 2012; Karachi Keamari gas leak 2020.",
        "(2) Transport and Infrastructure Risks": "Road fatality rates, bridge failures, rail accidents.",
        "(3) Maritime Disasters": "Fishing vessel losses, port incidents.",
        "(4) Oil Spills": "Tasman Spirit 2003, Clifton beach.",
        "(5) Fires": "Urban market fires, forest fires (Margalla, Sherani 2022).",
        "(6) Encroachments": "Settlements in riverbeds and floodplains (Swat, Nullah Lai).",
        "(7) Food Security": "~37% food insecure; flood-induced crop loss.",
        "(8) Population Bulge": "241M (2023 census), 2.55% growth.",
        "(9) Biological Hazards": "Dengue, COVID-19, locust outbreak 2020, polio.",
    },
}

VULNERABILITY = {
    "(A) Population Pressure and Diverse Terrains": "Rapid urbanization, settlements across floodplains, mountains, deserts and coast.",
    "(B) Vulnerable Settlements and Infrastructure Deficits": "Katcha housing, weak drainage, unregulated construction, ageing embankments.",
    "(C) Institutional Vulnerabilities": ["Delayed Decision-Making", "Operational Confusion", "Public Distrust", "Resource Misallocation"],
    "(D) Socio-Economic Stratification Amplifying Risk": ["Poverty", "Income inequality",
        "Limited access to education, healthcare and emergency resources", "Resource Disparities", "Spatial Entrapment",
        "Unequal Mobility", "Marginalized communities", "Poor households", "Institutional Neglect"],
}

EMERGING_RISKS = {
    "(A) Pakistan's Vulnerability - Global Climate Risk Index (CRI) 2025": "Germanwatch CRI 2025 ranks Pakistan among the most affected countries, driven by the 2022 floods (~USD 30 bn losses & damages, 1,700+ deaths).",
    "(B) Increasing GLOF Risks": "Rising temperatures have destabilized moraine-dammed lakes, increasing the likelihood of sudden breaches. GLOFs pose immediate threats to downstream settlements, hydroelectric infrastructure and the Karakoram Highway. GB and parts of KP are witnessing an alarming increase in glacial lake formation. Lessons from 2025 Taalidass, Ghizer Lake and the 2010 Attabad Lake disaster highlight the need for proactive mitigation, remote-sensing monitoring and early-warning systems.",
    "(C) Erratic Monsoons and Shifting Precipitation Patterns": "Early onset & extended seasons, uneven 'short burst' rainfall, and high-intensity phenomena (cloudbursts, intense downpours, hailstorms, atmospheric instability) cause flash floods, mudflows, riverine flooding and soil erosion.",
    "(D) Sea Intrusion and Coastal Salinization": "Rising sea levels along the 1,050 km coast compound flood risk in Southern Sindh and Balochistan. Saltwater intrusion degrades arable land. Karachi, Gwadar and Thatta face tidal surges and cyclones amplified by poor drainage. Remedies: integrated coastal zone management, mangrove restoration, storm-surge early warning.",
}

SCENARIOS = [
    {"Scenario": "(A) Baseline", "Description": "Normal monsoon (±10% of average), routine river flows.",
     "Features": "Localized urban flooding, minor flash floods, seasonal heatwaves; ~0.5-1M affected; provincial PDMAs cope."},
    {"Scenario": "(B) Medium", "Description": "Above-normal monsoon (+25-40%), 1-2 GLOF events, high flood in one or two rivers.",
     "Features": "Breaches in embankments, 3-8M affected, crop losses in Punjab/Sindh, KKH disruption, NDMA coordination."},
    {"Scenario": "(C) Worst-Case", "Description": "Super flood (2022-type, +190% rainfall) combined with heatwave-driven glacier melt and cyclone/earthquake.",
     "Features": "30M+ affected, 1/3 of country inundated, loss of storage/hydropower, food insecurity, disease outbreak, international appeal."},
]

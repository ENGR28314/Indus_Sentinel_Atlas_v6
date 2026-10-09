"""Socio-Economic, Agro-Economic and Geo-Political & Strategic domain content."""
import pandas as pd

SOCIO_ECONOMIC = {
    "Food Security": "Indus waters irrigate ~90% of food production; wheat, rice, sugarcane depend on canal supply.",
    "Employment": "Agriculture employs ~37% of the labour force; water-linked sectors (textile, fisheries) add more.",
    "Urban Growth": "Karachi, Lahore, Faisalabad expanding rapidly; rising municipal demand and wastewater.",
    "Tourism": "Northern lakes, peaks and valleys draw millions; GB/KPK tourism economy depends on stable climate & roads.",
    "Domestic & Industrial Utility": "K-IV for Karachi, groundwater over-extraction in Lahore; industrial effluent challenges.",
    "Climate & Vulnerability": "Floods/droughts erode household assets; 2022 floods pushed ~9M into poverty.",
    "Energy Generation": "Hydropower ~25-30% of electricity (approx. 10,600+ MW installed); low-cost, renewable baseload.",
}

AGRO_ECONOMIC = {
    "World's Largest Irrigation (IBIS)": "Indus Basin Irrigation System: 3 major reservoirs, 19 barrages/headworks, 12 link canals, 45 canal commands, ~56,000 km canals, ~1.6 lakh watercourses, ~18 M ha irrigated.",
    "Crop Cultivation": "Kharif: cotton, rice, sugarcane, maize. Rabi: wheat, gram, oilseeds. Punjab ~75% of wheat.",
    "Rural Livelihoods": "~62% of population rural; livestock contributes ~60% of agricultural value added.",
    "GDP & Employment Contribution": "Agriculture ~23-24% of GDP and ~37% employment; major export earner via textiles.",
}

CROPS = pd.DataFrame({
    "Crop": ["Wheat", "Rice", "Cotton", "Sugarcane", "Maize"],
    "Production_Mt_approx": [28.0, 9.8, 1.4, 84.0, 9.8],
    "Season": ["Rabi", "Kharif", "Kharif", "Annual", "Kharif/Rabi"],
})

GEOPOLITICS = {
    "The Hydro-Politics of Kashmir": "The western rivers (Indus, Jhelum, Chenab) originate in or pass through Jammu & Kashmir, making the region central to Pakistan's water security and the wider dispute.",
    "The Indus Waters Treaty (IWT) Crisis": "1960 World Bank-brokered treaty gave eastern rivers (Ravi, Beas, Sutlej) to India and western rivers to Pakistan. In April 2025 India declared it would hold the treaty 'in abeyance'; Pakistan termed any stoppage of water an 'act of war' and maintains the treaty has no unilateral exit clause.",
    "Maritime Trade Infrastructure": "Karachi Port, Port Qasim and Gwadar (CPEC) - over 90% of trade is seaborne; Arabian Sea security & Makran coast development.",
}

CHENAB_IMPACTS = {
    "Flow Reductions at Head Marala": "Upstream flushing/filling of Baglihar & Salal reservoirs and sudden releases have caused abrupt drops (reported to tens of thousands of cusecs) at Marala, disrupting UCC & Marala-Ravi Link supply.",
    "Devastating Crop Impacts": "Rice (Kalar belt - Sialkot, Gujranwala, Narowal) and wheat sowing suffer from shortages at critical stages; sudden surges also cause flood damage.",
}

DIAMER_BHASHA = {
    "Joint Engineering and Progress": "272 m RCC dam on the Indus; main dam awarded 2020 to Power China-FWO JV; diversion and access works progressing.",
    "Strategic Storage and Economic Injection": "~8.1 MAF gross storage (6.4 MAF live), extends Tarbela life, adds ~35 days storage; ~4,500 MW; thousands of jobs in GB/KPK.",
    "The Power Postponement": "Power-generation component deferred/phased because of financing constraints; storage prioritised; completion targets slipped to ~2029+.",
}

PROVINCIAL_DISPUTE = {
    "Sindh's Grievances (Lower Riparian)": "Shortages under the 1991 Water Apportionment Accord, below-Kotri flows needed for the delta (Accord recommends 10 MAF), opposition to Kalabagh and new canals (e.g. Cholistan canals 2025), allegations of Chashma-Jhelum and Taunsa-Panjnad link misuse.",
    "Punjab's Counter-Claims (Upper Riparian)": "Argues historic uses, system losses in Sindh, telemetry disputes, and need for new storage for food security of the whole country.",
    "Structural Gridlocks / Deadlock": "Absence of trusted real-time telemetry, disputed 'three-tier' shortage formula, and politicised IRSA membership.",
}

LEGAL_MECHANISMS = {
    "IRSA Technocratic Vote Deadlock": "Indus River System Authority (IRSA Act 1992) decides by majority; ties among provincial members stall decisions on shortages and canal NOCs.",
    "Council of Common Interests (CCI) Appeal": "Under Art. 155 of the Constitution, an aggrieved province may complain to the CCI; its decision is binding.",
    "Constitutional Review (Supreme Court)": "Art. 184(3) / 199 jurisdiction to interpret the Accord, IRSA Act and CCI decisions.",
    "The 2024-2026 Restructuring Crisis": "Proposals to amend IRSA composition and the Cholistan/new-canal NOC triggered protests in Sindh; CCI (Apr 2025) deferred new canals pending consensus.",
    "The Veto Power and Conciliation": "No province holds a formal veto, but CCI consensus practice and Parliament joint sitting provide conciliation pathways.",
    "Judicial Intervention": "Courts have intervened on water rights, environmental flows (Ravi, delta) and dam funding (Diamer-Bhasha fund 2018).",
}

CHINA_HYDRO = {
    "Dominant Share of FDI": "China is Pakistan's largest FDI source; CPEC energy projects (~USD 20+ bn) dominate, with hydropower under IPP mode via China Three Gorges (CTG) and other SOEs.",
}

HYDRO_ASSETS = pd.DataFrame([
    ["Karot Hydropower Project", 720, "Jhelum", "Punjab/AJK", "China Three Gorges (CTG) / CSAIL", 1.74, "Commercial operation June 2022"],
    ["Suki Kinari (SK) Hydropower Station", 884, "Kunhar", "KPK (Mansehra)", "CGGC / SK Hydro", 1.96, "Commercial operation 2024"],
    ["Kohala Hydropower Project", 1124, "Jhelum", "AJK", "CTG", 2.40, "Planned / financing stage"],
    ["Azad Pattan Hydropower Project", 700.7, "Jhelum", "AJK/Punjab", "CGGC / Alamgir Power", 1.54, "Planned / financing stage"],
], columns=["Project", "Capacity_MW", "River", "Location", "Sponsor", "Cost_USD_bn_approx", "Status"])

INDIA_DESIGNS = {
    "Pakal Dul (1,000 MW) - Marusudar (Chenab trib.)": {
        "Pondage Capacity": ("Storage of ~0.1 MAF (~125 MCM) with a 167 m CFRD dam.", "Pakistan views it as exceeding IWT Annexure D/E limits, enabling manipulation of flow timing."),
        "Freeboard Height & Dam Elevation": ("Freeboard higher than design flood requirements.", "Excess freeboard allows raising storage above treaty-permissible levels."),
        "Deep-Level Outlets and Gated Spillways": ("Low-level outlets & gated spillways below Dead Storage Level.", "Enables drawdown flushing and potential control of flows beyond run-of-river."),
    },
    "Ratle (850 MW) - Chenab": {
        "Pondage Capacity": ("Pondage of ~24 MCM proposed.", "Pakistan says it is about 3x larger than needed for firm power under Annex D."),
        "Freeboard Height & Dam Elevation": ("Freeboard of ~2 m above max reservoir level.", "Pakistan contends 1 m is adequate; extra height adds storage."),
        "Deep-Level Outlets and Gated Spillways": ("Gated spillway crest ~ 20-30 m below full pond; low-level outlets.", "Pakistan argues for ungated/higher spillways as in the Kishenganga Award logic."),
    },
}

COA_INTERVENTIONS = [
    "2016: Pakistan requested a Court of Arbitration (CoA); India sought a Neutral Expert - World Bank 'paused' then (2022) activated both processes.",
    "Jul 2023: CoA (PCA, The Hague) unanimously upheld its competence despite India's boycott.",
    "Jun 2025: CoA Supplemental Award - India's 'abeyance' of IWT does not affect the Court's competence; treaty cannot be unilaterally suspended.",
    "Aug 2025: CoA Award on general interpretation - India must 'let flow' western rivers; design criteria for run-of-river plants (pondage, freeboard, outlets, spillways) to be strictly interpreted.",
    "Neutral Expert (Michel Lino) proceedings continue on technical 'differences' for Kishenganga & Ratle.",
]

"""UN SDGs, MDGs and Pakistan Vision 2025/2030 agenda relevant to water, food and environment."""
import pandas as pd

MDGS = pd.DataFrame([
    ["MDG 1", "Eradicate extreme poverty and hunger", "Partially met - poverty fell but stunting remained high"],
    ["MDG 7", "Ensure environmental sustainability", "Off-track on forest cover; progress on improved water sources"],
    ["MDG 8", "Global partnership for development", "Mixed"],
], columns=["Goal", "Title", "Pakistan outcome (2015)"])

SDGS = pd.DataFrame([
    ["SDG 1", "No Poverty", "BISP/Ehsaas cash transfers; flood-resilient livelihoods"],
    ["SDG 2", "Zero Hunger", "Food security, irrigation efficiency, wheat/rice productivity, nutrition"],
    ["SDG 6", "Clean Water & Sanitation", "National Water Policy 2018, groundwater regulation, WASH"],
    ["SDG 7", "Affordable & Clean Energy", "Hydropower expansion, ARE Policy 2019 (60% clean by 2030)"],
    ["SDG 11", "Sustainable Cities", "Urban flood drainage, Karachi/Lahore resilience"],
    ["SDG 13", "Climate Action", "Updated NDC 2021 (50% emissions cut by 2030, 15% unconditional), NAP 2023"],
    ["SDG 14", "Life Below Water", "Mangrove restoration (Indus Delta), fisheries"],
    ["SDG 15", "Life on Land", "Ten Billion Tree Tsunami, protected areas expansion"],
], columns=["Goal", "Title", "Pakistan relevance"])

VISION_AGENDA = {
    "Food": "Raise crop yields, lining of watercourses, high-efficiency irrigation, strategic grain reserves.",
    "Water Conservation": "Build storage (Diamer-Bhasha, Mohmand), recharge aquifers, telemetry, reduce conveyance losses (~40%).",
    "Environmental Protection": "Protected areas 15%+, smog action plans, effluent treatment, Recharge Pakistan.",
    "Sustainable Development": "Climate-resilient infrastructure (4RF after 2022 floods), green CPEC.",
    "Zero Hunger": "Targeted subsidies, Kissan cards, nutrition-sensitive agriculture.",
    "Poverty Alleviation": "Social protection, microfinance, rural employment via livestock, apiculture & aquaculture.",
}

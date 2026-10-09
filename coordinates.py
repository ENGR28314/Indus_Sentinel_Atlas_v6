"""Approximate geographic coordinates (lat, lon) for Pakistan's water & terrain features."""

PROVINCES = {
    "Gilgit-Baltistan": (35.80, 74.98),
    "Khyber Pakhtunkhwa (KPK)": (34.95, 72.33),
    "Punjab": (31.17, 72.70),
    "Sindh": (25.89, 68.52),
    "Balochistan": (28.49, 65.10),
    "Azad Jammu and Kashmir": (33.92, 73.78),
    "Islamabad Capital Territory (ICT)": (33.68, 73.05),
}

DAMS = {
    "Tarbela Dam": (34.09, 72.70),
    "Mangla Dam": (33.14, 73.64),
    "Warsak Dam": (34.17, 71.36),
    "Khanpur Dam": (33.80, 72.93),
    "Rawal Dam": (33.70, 73.12),
    "Simly Dam": (33.72, 73.34),
    "Hub Dam": (25.25, 67.12),
    "Mirani Dam": (26.07, 62.73),
    "Gomal Zam Dam": (32.10, 69.87),
    "Diamer-Bhasha Dam (u/c)": (35.52, 73.74),
    "Mohmand Dam (u/c)": (34.37, 71.53),
    "Dasu Dam (u/c)": (35.29, 73.21),
    "Neelum-Jhelum HPP": (34.38, 73.62),
    "Karot HPP": (33.61, 73.60),
    "Suki Kinari HPP": (34.83, 73.50),
    "Kohala HPP (planned)": (34.10, 73.50),
    "Azad Pattan HPP (planned)": (33.73, 73.58),
}

BARRAGES = {
    "Jinnah Barrage": (32.92, 71.52),
    "Chashma Barrage": (32.43, 71.38),
    "Taunsa Barrage": (30.51, 70.85),
    "Guddu Barrage": (28.42, 69.71),
    "Sukkur Barrage": (27.68, 68.85),
    "Kotri Barrage": (25.37, 68.31),
    "Marala Headworks": (32.67, 74.46),
    "Khanki Headworks": (32.40, 73.97),
    "Qadirabad Barrage": (32.32, 73.68),
    "Trimmu Barrage": (31.15, 72.15),
    "Panjnad Headworks": (29.35, 71.03),
    "Rasul Barrage": (32.68, 73.53),
    "Balloki Headworks": (31.22, 73.86),
    "Sulemanki Headworks": (30.38, 73.87),
    "Islam Headworks": (29.83, 72.55),
    "Sidhnai Barrage": (30.57, 72.13),
}

CONFLUENCES = {
    "Indus-Gilgit (Jaglot)": (35.76, 74.62),
    "Indus-Kabul (Attock)": (33.90, 72.23),
    "Jhelum-Chenab (Trimmu)": (31.15, 72.15),
    "Ravi-Chenab (near Ahmadpur Sial)": (30.60, 71.82),
    "Sutlej-Chenab (Panjnad)": (29.35, 71.03),
    "Panjnad-Indus (Mithankot)": (28.95, 70.37),
    "Hunza-Gilgit (Gilgit)": (35.92, 74.36),
    "Swat-Kabul (Charsadda)": (34.12, 71.73),
}

LAKES = {
    "Saif-ul-Malook": (34.88, 73.69), "Attabad Lake": (36.32, 74.86),
    "Satpara Lake": (35.23, 75.63), "Sheosar Lake": (34.99, 75.23),
    "Keenjhar Lake": (24.94, 68.05), "Manchar Lake": (26.42, 67.67),
    "Haleji Lake": (24.80, 67.77), "Hanna Lake": (30.25, 67.10),
    "Kalar Kahar Lake": (32.78, 72.70), "Rawal Lake": (33.70, 73.12),
    "Banjosa Lake": (33.78, 73.81), "Lulusar Lake": (35.08, 73.93),
    "Mahodand Lake": (35.75, 72.62), "Kachura Lakes": (35.42, 75.45),
    "Rama Lake": (35.36, 74.81), "Borith Lake": (36.43, 74.86),
    "Karambar Lake": (36.88, 73.72), "Ansoo Lake": (34.88, 73.79),
    "Uchhali Lake": (32.56, 72.02), "Namal Lake": (32.67, 71.80),
    "Hamal Lake": (27.40, 67.50), "Zangi Nawar Lake": (29.45, 63.70),
}

PEAKS = {
    "K2 (8,611 m) - Karakoram": (35.88, 76.51),
    "Nanga Parbat (8,126 m) - Himalaya": (35.24, 74.59),
    "Tirich Mir (7,708 m) - Hindu Kush": (36.25, 71.84),
    "Koyo Zom (6,872 m) - Hindu Raj": (36.55, 73.04),
    "Sikaram (4,755 m) - Spin Ghar": (33.98, 70.08),
    "Takht-e-Sulaiman (3,487 m) - Sulaiman": (31.57, 69.97),
    "Zarghun Ghar (3,578 m) - Toba Kakar area": (30.33, 67.33),
    "Zardak Peak (2,260 m) - Kirthar": (27.05, 67.20),
    "Sakesar (1,522 m) - Salt Range": (32.53, 71.94),
}

RIVER_PATHS = {
    "Indus": [(35.70, 76.20), (35.30, 75.60), (35.76, 74.62), (35.40, 73.20),
              (34.09, 72.70), (33.90, 72.23), (32.92, 71.52), (32.43, 71.38),
              (30.51, 70.85), (28.95, 70.37), (28.42, 69.71), (27.68, 68.85),
              (25.37, 68.31), (24.10, 67.40)],
    "Jhelum": [(34.20, 74.30), (34.38, 73.62), (33.61, 73.60), (33.14, 73.64),
               (32.68, 73.53), (32.00, 72.80), (31.15, 72.15)],
    "Chenab": [(32.67, 74.46), (32.32, 73.68), (31.15, 72.15), (30.60, 71.82), (29.35, 71.03)],
    "Ravi": [(32.20, 75.30), (31.55, 74.30), (31.22, 73.86), (30.57, 72.13), (30.60, 71.82)],
    "Sutlej": [(31.00, 74.60), (30.38, 73.87), (29.83, 72.55), (29.35, 71.03)],
    "Kabul": [(34.17, 71.36), (34.12, 71.73), (33.90, 72.23)],
}

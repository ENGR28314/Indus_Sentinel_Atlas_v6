# Indus Sentinel: Pakistan Hydro-Strategic & Disaster Risk Atlas

**Created and Designed by: Engr. Syed Hassan Iqbal Shah**

Interactive atlas of Pakistan's provinces (GB, KPK, Punjab, Sindh, Balochistan, AJK, ICT): rivers, dams, barrages,
link canals, confluences, climatic regions, mountain ranges & peaks, lakes, National Disaster Risk Context,
socio-economic / agro-economic / geo-political domains, IRSA legal mechanisms, Chinese hydropower investments,
India's Pakal Dul & Ratle designs and Court of Arbitration interventions.

## Run
```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Files
| File | Purpose |
|---|---|
| app.py | Streamlit UI and navigation |
| coordinates.py | Lat/long of provinces, dams, barrages, confluences, lakes, peaks, river paths |
| data_loader.py | Provinces, rivers, dams, link canals, climate regions, mountain ranges, lakes |
| hazards.py | Hazard profile, vulnerability, emerging risks, risk scenarios |
| domains.py | Socio-economic, agro-economic, geo-political, IRSA, China hydropower, Pakal Dul/Ratle, CoA |
| hydraulic_model.py | Manning flow, reservoir balance, flood travel time |
| map_view.py | Folium map |
| network_view.py | Indus Basin upstream-downstream schematic |
| simulation_engine.py | Basin stress, Water Quality Index, hazard classes, flash-flood synthesizer |
| test_suite.py | Automated tests: `python -m unittest test_suite.py` |
| forests_parks.py | Forest types, notable forests, national parks (with map coordinates) |
| agro_inputs.py | Rabi/Kharif seasons, apiculture, aquaculture, editable input data & charts |
| indian_projects.py | Indian Atrocities tab: canals, disputed designs, Neutral Expert timeline |
| sustainability.py | UN SDGs, MDGs, Vision 2030 agenda |
| maps_extra.py | Thematic maps: geo-political, China hydropower, Indian projects, hazards, climate, link canals, risk; schematics |
| sebal_model.py | SEBAL evapotranspiration: offline NumPy model + Google Earth Engine (Landsat 8/9, HydroSHEDS), geemap maps, geopandas sub-basin stats |\n| references.py | Sources list |
| __pycache__/*.cpython-*.pyc | Pre-compiled bytecode (optional; Python regenerates automatically) |

Data is approximate and for education; verify with WAPDA, IRSA, NDMA, PMD and PCA records for official use.
\n## SEBAL on Google Earth Engine\n1. Sign up at https://earthengine.google.com and register a Google Cloud project.\n2. Run `earthengine authenticate`.\n3. In the app open **SEBAL Evapotranspiration > Google Earth Engine**, enter your project ID, pick dates, press Run.\n
## AI ET Review
Page "🤖 AI ET Review": submit SEBAL ET results per sub-basin (form or CSV), get rule-based anomaly flags, and an AI explanation via Lovable AI Gateway (`openai/gpt-6-astra`). Set `LOVABLE_API_KEY` as an environment variable or in `.streamlit/secrets.toml`. Submissions are stored in `data/et_submissions.csv`.

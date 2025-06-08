
# OECD Patent Dashboard

This repository contains all necessary files to run the interactive dashboard for analysing OECD patent statistics.

## 📁 Files Included

- `preprocess_patent_data.py`: Script to load and clean the raw OECD patent dataset.
- `cleaned_oecd_patent_data.csv`: The cleaned dataset after preprocessing.
- `dashboard_final.py`: Streamlit dashboard implementation with interactive visualisations.

## ⚙️ How to Run

1. Make sure you have Python installed.
2. Install required packages:
```bash
pip install streamlit pandas plotly
```

3. Run the Streamlit dashboard:
```bash
streamlit run dashboard_final.py
```

## 📊 Dashboard Features

- **Filtering** by Year, Country, Tech Domain, Measure Type.
- **Bar Chart**: Patent count over time.
- **Line Chart**: Trends per country.
- **Heatmap**: Country vs. Tech Domain.
- **Pie Chart**: Share of patents by Measure Type.
- **Animated Bar Chart**: Country rankings over time.
- **Treemap**: Latest year’s country share.

## ✅ Interactions Implemented

- **Dynamic filtering**: Sidebar filters affect all graphs.
- **Hover tooltips**: Interactive tooltips on all charts.
- **Auto updates**: All charts auto-refresh with user selection.

## 📄 Dataset Source

OECD Patent statistics and indicators – https://data-explorer.oecd.org

Released: March 12, 2025

---

For any questions, contact: 104856650@student.swin.edu.au
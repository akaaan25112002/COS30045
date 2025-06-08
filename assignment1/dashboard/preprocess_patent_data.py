import pandas as pd

# Read the original data from the OECD CSV file
df = pd.read_csv("OECD.STI.PIE,DSD_PATENTS@DF_PATENTS,1.0+.A...PRIORITY...INVENTOR..._T.csv")

# Select and rename important columns
df_cleaned = df[[
    'TIME_PERIOD',
    'OBS_VALUE',
    'PATENT_AUTHORITIES',
    'OECD_TECHNOLOGY_PATENT',
    'REF_AREA',
    'MEASURE'
]].rename(columns={
    'TIME_PERIOD': 'Year',
    'OBS_VALUE': 'Patent_Count',
    'PATENT_AUTHORITIES': 'Patent_Office',
    'OECD_TECHNOLOGY_PATENT': 'Tech_Domain',
    'REF_AREA': 'Country',
    'MEASURE': 'Measure_Type'
})

# Remove missing values
df_cleaned.dropna(subset=['Year', 'Patent_Count', 'Country', 'Tech_Domain'], inplace=True)

# Convert data types and filter the dataset
df_cleaned['Year'] = pd.to_numeric(df_cleaned['Year'], errors='coerce')
df_cleaned['Patent_Count'] = pd.to_numeric(df_cleaned['Patent_Count'], errors='coerce')
df_cleaned = df_cleaned[(df_cleaned['Year'] >= 2010) & (df_cleaned['Patent_Count'] >= 0)]

# Export to CSV file
df_cleaned.to_csv("cleaned_oecd_patent_data.csv", index=False)

print("✅ Data has been cleaned and saved to cleaned_oecd_patent_data.csv")
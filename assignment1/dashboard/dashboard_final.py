import streamlit as st
st.set_page_config(page_title="OECD Patent Dashboard", layout="wide")

import pandas as pd
import plotly.express as px

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("assignment1/dashboard/cleaned_oecd_patent_data.csv")

df = load_data()

# SIDEBAR - Filters
st.sidebar.header("🔍 Filters")
years = sorted(df["Year"].unique())
countries = sorted(df["Country"].unique())

selected_years = st.sidebar.multiselect("Select year(s):", years, default=years[-5:])
selected_countries = st.sidebar.multiselect("Select country/countries:", countries, default=["USA", "CHN", "DEU", "JPN", "KOR"])

filtered_df = df[
    (df["Year"].isin(selected_years)) &
    (df["Country"].isin(selected_countries))
]

# MAIN TITLE
st.title("📊 OECD Patent Dashboard")
st.markdown("**Analysis of environmental innovation based on OECD patent data.**")
st.markdown("Use the filters on the left to explore data by year, country, technology domain, and measure type.")
st.markdown("**Create by Nguyen Anh Khoa - 104856650**")
# CHART 1: Total patents by year
st.subheader("📈 Total Patents Over Time")
fig1 = px.bar(
    filtered_df.groupby("Year")["Patent_Count"].sum().reset_index(),
    x="Year", y="Patent_Count",
    labels={"Patent_Count": "Patent Count"},
    color="Year"
)
st.plotly_chart(fig1, use_container_width=True)

# CHART 2: Patents by country over time
st.subheader("🌍 Patents by Country Over Time")
fig2 = px.line(
    filtered_df.groupby(["Year", "Country"])["Patent_Count"].sum().reset_index(),
    x="Year", y="Patent_Count", color="Country", markers=True,
    labels={"Patent_Count": "Patent Count"}
)
st.plotly_chart(fig2, use_container_width=True)

# CHART 3: Heatmap of countries and tech domains
st.subheader("🔬 Relationship Between Country and Technology Domain")
heatmap_df = filtered_df.groupby(["Country", "Tech_Domain"])["Patent_Count"].sum().reset_index()
heatmap_df_pivot = heatmap_df.pivot(index="Tech_Domain", columns="Country", values="Patent_Count").fillna(0)

fig3 = px.imshow(
    heatmap_df_pivot,
    labels=dict(x="Country", y="Technology Domain", color="Patent Count"),
    aspect="auto"
)
st.plotly_chart(fig3, use_container_width=True)

# CHART 4: Patent share by measure type
st.subheader("📊 Distribution of Patents by Measure Type")
pie_df = filtered_df.groupby("Measure_Type")["Patent_Count"].sum().reset_index()
fig4 = px.pie(
    pie_df, names="Measure_Type", values="Patent_Count",
    title="Share of Patents by Measure Type"
)
st.plotly_chart(fig4, use_container_width=True)

# CHART 5: Animated bar chart by year and country
st.subheader("🎞️ Animated Patent Chart by Year and Country")
fig5 = px.bar(
    filtered_df,
    x="Country", y="Patent_Count", color="Tech_Domain",
    animation_frame="Year", animation_group="Country",
    labels={"Patent_Count": "Patent Count"},
    height=500
)
st.plotly_chart(fig5, use_container_width=True)

# CHART 6: Treemap of patents by country (latest year)
st.subheader("🌲 Treemap: Patent Share by Country")
latest_year = filtered_df["Year"].max()
latest_data = filtered_df[filtered_df["Year"] == latest_year]
fig_treemap = px.treemap(latest_data, path=["Country"], values="Patent_Count")
st.plotly_chart(fig_treemap, use_container_width=True)
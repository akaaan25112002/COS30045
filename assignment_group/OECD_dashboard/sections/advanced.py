import streamlit as st
import pandas as pd
import plotly.express as px
from utils.db import load_table
from advanced_single_country import single_country_report
from advanced_compare_countries import compare_countries_report


def section_advanced():
    st.header("📊 Advanced Dashboard: Custom Country & Trend Reports")

    option = st.radio("Choose Analysis Mode", [
        "📌 Single Country Report",
        "🌍 Compare Multiple Countries"
    ])

    if option == "📌 Single Country Report":
        single_country_report()
    elif option == "🌍 Compare Multiple Countries":
        compare_countries_report()

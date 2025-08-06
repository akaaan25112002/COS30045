import streamlit as st
from sections import intro, environment, emissions, area, water, energy, advanced
#, water, energy, advanced, summary
st.set_page_config(page_title="OECD Dashboard", layout="wide")

section = st.sidebar.radio("📊 Select Section", [
    "1. Introduction",
    "2. Environmental Impact",
    "3. Emissions & Chemicals",
    "4. Land Use",
    "5. Water Use",
    "6. Energy Use",
    "7. Advanced Analysis",
    "8. Summary"
])

if section == "1. Introduction":
    intro.section_intro()
elif section == "2. Environmental Impact":
    environment.section_environment()
elif section == "3. Emissions & Chemicals":
    emissions.section_emissions()
elif section == "4. Land Use":
    area.section_area()
elif section == "5. Water Use":
    water.section_water()
elif section == "6. Energy Use":
    energy.section_energy()
elif section == "7. Advanced Analysis":
    advanced.section_advanced()
elif section == "8. Summary":
    summary.section_summary()
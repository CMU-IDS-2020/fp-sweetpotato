# LYDIA SCHWEITZER Assignment 4
# Landing Site Analysis application using Streamlit
# data pulled from Planetary Data Sciences node:
# https://pds-geosciences.wustl.edu/lro/lro-l-lola-3-rdr-v1/lrolol_1xxx/data/lola_gdr/polar/jp2/
# machine learning code for crater identification pulled from:
# 


import introPage
import individualMaps01
import viableMaps
import opsPlanning
import streamlit as st

# wide configuration
st.beta_set_page_config(layout="wide")

# # variables
# savedImages = dict()

# tabs
tabs = {
    "Intro to Site Analysis": introPage,
    "Individual Map View": individualMaps01,
    "Viable Terrain": viableMaps,
    "Operation Planning": opsPlanning
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Menu", list(tabs.keys()))
tab = tabs[selection]
tab.run()

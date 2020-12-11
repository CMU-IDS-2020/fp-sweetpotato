# individual map view 
# LCS
# sweetpotato

import streamlit as st
import individualMaps_layered
import individualMaps_sbs

def run():

    st.title("Lunar Map Analysis")

    # show global or local maps
    modes = {
        'Side-by-Side': individualMaps_sbs,
        'Layered': individualMaps_layered
    }
    selection = st.sidebar.radio("Select Mode", list(modes.keys()))
    mode = modes[selection]
    mode.run()



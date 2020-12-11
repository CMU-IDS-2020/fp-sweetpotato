# info/intro page 
# LCS
# sweetpotato

import streamlit as st


analysisTextRaw = open("text/aboutSiteAnalysis.txt")
analysisText = analysisTextRaw.read()

aboutAppRaw = open("text/aboutApp.txt")
aboutApp = aboutAppRaw.read()

def run():
    st.title("Lunar Mission Site Analysis")
    st.write(analysisText)
    st.image("images/three_mission.jpg", use_column_width = True)
    st.write(aboutApp)


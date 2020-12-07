# individual map view -- SIDE BY SIDE 
# LCS
# sweetpotato

import streamlit as st
from PIL import Image
import copy

################################################################################
# DATA SETUP
################################################################################
views = ['Local', 'Global']
names = ['Illumination', 'Slope', 'Ice Stability at Depth']

# Global Maps for introduction/informaiton/background
globalElevation = Image.open("images/globalElevation.jpg")
globalIllumination = Image.open("images/globalIllumination.jpg")
globalSlope = Image.open("images/globalSlope.jpg")
globalIceStability = Image.open("images/globalIceStability.jpg")

# Individual zoomed maps for specific site
localIllumination = Image.open("images/localIllumination.jpg")
localSlope = Image.open("images/localSlope.jpg")
localIceStability = Image.open("images/localIceStability.jpg")

################################################################################
# TEXT & ORGANIZATION
################################################################################
localText = '''Local maps show a prospective landing region at the lunar south pole. 
All maps are ~5x5 kilometers.'''
globalText = '''Global maps show the south pole region out to ~85 deg latitude.
All maps are 300x300 kilometers.'''

illuminationTextRaw = open('text/illuminationText.txt')
illuminationText = illuminationTextRaw.read()
slopeTextRaw = open('text/slopeText.txt')
slopeText = slopeTextRaw.read()
iceTextRaw = open('text/iceText.txt')
iceText = iceTextRaw.read()

viewInfo = {
    'Local': [[localIllumination, localSlope, localIceStability], localText],
    'Global': [[globalIllumination, globalSlope, globalIceStability], globalText]
}

infoText = {
    'Illumination': illuminationText,
    'Slope': slopeText,
    'Ice Stability at Depth': iceText 
} 


################################################################################
# SUPPORTING FUNCTIONS
################################################################################
def displayDetailed(name, image, row):
    row.image(image, use_column_width = True)
    st.sidebar.title(name)
    st.sidebar.write(infoText[name])


################################################################################
# MAIN RUN
################################################################################
def run():
    view = st.selectbox("Select View", views)

    st.write(viewInfo[view][1])
    st.write("** To view an image in full screen, hover over it and select the double arrows in the top right corner.")

    col1, col2 = st.beta_columns([1, 3.75])
    images = viewInfo[view][0]

    col1.title('')

    col1.image(images[0], use_column_width = True)
    col1.image(images[1], use_column_width = True)
    col1.image(images[2], use_column_width = True)
    
    illuminationButton = st.sidebar.button('Illumination')
    slopeButton = st.sidebar.button('Slope')
    iceButton = st.sidebar.button('Ice Stability')
    
    if illuminationButton:
        displayDetailed('Illumination', images[0], col2)
    if slopeButton:
        displayDetailed('Slope', images[1], col2)
    if iceButton:
        displayDetailed('Ice Stability at Depth', images[2], col2)

    
    
    

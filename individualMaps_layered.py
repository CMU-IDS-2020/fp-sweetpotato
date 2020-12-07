# individual map view -- LAYERED
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

localText = '''Local maps show a prospective landing region at the lunar south pole. 
\nAll maps are ~5x5 kilometers.'''
globalText = '''Global maps show the south pole region out to ~85 deg latitude.
\nAll maps are 300x300 kilometers.'''

# Global Maps for introduction/informaiton/background
globalElevation = Image.open("images/globalElevation.jpg")
globalIllumination = Image.open("images/globalIllumination.jpg")
globalSlope = Image.open("images/globalSlope.jpg")
globalIceStability = Image.open("images/globalIceStability.jpg")

# Individual zoomed maps for specific site
localIllumination = Image.open("images/localIllumination.jpg")
localSlope = Image.open("images/localSlope.jpg")
localIceStability = Image.open("images/localIceStability.jpg")


viewInfo = {
    'Local': [[localIllumination, localSlope, localIceStability], localText],
    'Global': [[globalIllumination, globalSlope, globalIceStability], globalText]
}

################################################################################
# SUPPORTING FUNCTIONS
################################################################################
def addLayers(image1, image2, image3):
    # st.image(image1)
    # if st.checkbox('Add Layer 2'):
    #     st.image(image2)

    # newImage1 = Image.blend(image1, image2, 1)
    # newImage2 = Image.blend(newImage1, image3, 1)

    newImage = copy.copy(image1)

    newImage.paste(image2, (0,0), image2)
    newImage.paste(image3, (0,0), image3)
    return newImage

################################################################################
# MAIN RUN
################################################################################
def run():
    #st.image(globalElevation)

    view = st.selectbox("Select View", views)

    images = viewInfo[view][0]
    st.sidebar.subheader('Layer 1')
    map1 = st.sidebar.selectbox('Map', names, key = 'Layer 1')
    map1A = st.sidebar.slider('Opacity', 100, (0), key = 'Layer 1')
    image1 = copy.copy(images[names.index(map1)])
    image1.putalpha(int(256*(map1A/100)))

    st.sidebar.subheader('Layer 2')
    map2 = st.sidebar.selectbox('Map', names, key = 'Layer 2')
    map2A = st.sidebar.slider('Opacity', 100, (0), key = 'Layer 2')
    image2 = copy.copy(images[names.index(map2)])
    image2.putalpha(int(256*(map2A/100)))

    st.sidebar.subheader('Layer 3')
    map3 = st.sidebar.selectbox('Map', names, key = 'Layer 3')
    map3A = st.sidebar.slider('Opacity', 100, (0), key = 'Layer 3')
    image3 = copy.copy(images[names.index(map3)])
    image3.putalpha(int(256*(map3A/100)))
  
    row1, ghostrow2 = st.beta_columns(2)
    finalImage = addLayers(image1, image2, image3)
    row1.image(finalImage)
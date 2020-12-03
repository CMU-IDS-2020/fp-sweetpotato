# individual map view 
# LCS
# sweetpotato

import streamlit as st
import imageData as imd
from PIL import Image

views = ['Local', 'Global']
modes = ["Side-by-Side", "Layered"]

localText = '''Local maps show a prospective landing region at the lunar south pole. 
\nAll maps are ~5x5 kilometers.'''

globalText = '''Global maps show the south pole region out to ~85 deg latitude.
\nAll maps are 300x300 kilometers.'''

names = ['Illumination', 'Slope', 'Ice Stability at Depth']

test = imd.localSlope

# Global Maps for introduction/informaiton/background
globalElevation = Image.open("images\globalElevation.jpg")
globalIllumination = Image.open("images\globalIllumination.jpg")
globalSlope = Image.open("images\globalSlope.jpg")
globalIceStability = Image.open("images\globalIceStability.jpg")

# Individual zoomed maps for specific site
localIllumination = Image.open("images\localIllumination.jpg")
localSlope = Image.open("images\localSlope.jpg")
localSlope.putalpha(100)
localIceStability = Image.open("images\localIceStability.jpg")

viewInfo = {
    'Local': [[imd.localIllumination, imd.localSlope, imd.localIceStability], localText],
    'Global': [[imd.globalIllumination, imd.globalSlope, imd.globalIceStability], globalText]
}


def displayLayered(view):
    images = viewInfo[view][0]
    st.sidebar.subheader('Layer 1')
    map1 = st.sidebar.selectbox('Map', names, key = 'Layer 1')
    map1A = st.sidebar.slider('Opacity', 100, (0), key = 'Layer 1')
    image1 = images[names.index(map1)]

    st.sidebar.subheader('Layer 2')
    map2 = st.sidebar.selectbox('Map', names, key = 'Layer 2')
    map2A = st.sidebar.slider('Opacity', 100, (0), key = 'Layer 2')
    image2 = images[names.index(map2)].putalpha(int(256*(map2A/100)))

    st.sidebar.subheader('Layer 3')
    map3 = st.sidebar.selectbox('Map', names, key = 'Layer 3')
    map3A = st.sidebar.slider('Opacity', 100, (0), key = 'Layer 3')
    image3 = images[names.index(map3)].putalpha(int(256*(map3A/100)))

    row1, row2 = st.beta_columns(2)    
    localIllumination.putalpha(int(256*(map1A/100)))
    row1.image(localIllumination)
    row1.image(localSlope)
    # row1.image(image3)
    # localIllumination.putalpha(int(256*(map1A/100)))
    # st.image(localIllumination)
    # st.image(localSlope)
    # st.image(image3)

def displaySbS(view):
    st.write(viewInfo[view][1])

    row1a, row1b, row1c = st.beta_columns(3)    #images
    images = viewInfo[view][0]

    row1a.image(images[0], use_column_width = True)
    row1b.image(images[1], use_column_width = True)
    row1c.image(images[2], use_column_width = True)

def run():
    st.title("Lunar Map Analysis")

    # show global or local maps
    view = st.selectbox("Select View", views)
    mode = st.sidebar.radio("Select Mode", modes)

    if mode == "Layered":
        displayLayered(view)
    else:
        displaySbS(view)

class SbSSettings(object):
    def __init__(self, mapInfoChecked):
        self.mapInfoChecked = False

class LSettings(object):
    def __init__(self, mapOrder):
        self.mapOrder = ['illumination', 'slope', 'ice']


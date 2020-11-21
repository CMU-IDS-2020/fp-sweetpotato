# LYDIA SCHWEITZER Assignment 4
# Landing Site Analysis application using Streamlit
# data pulled from Planetary Data Sciences node:
# https://pds-geosciences.wustl.edu/lro/lro-l-lola-3-rdr-v1/lrolol_1xxx/data/lola_gdr/polar/jp2/
# machine learning code for crater identification pulled from:
# 

# IMPORTS **********************************************************************
import streamlit as st
import copy
import pandas as pd
from PIL import Image
#from streamlit_drawable_canvas import st_canvas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import altair as alt
import pydeck as pdk
import warnings
warnings.filterwarnings('ignore')
# SETTING PAGE CONFIG TO WIDE MODE
st.beta_set_page_config(layout="wide")

################################################################################
# DATA SETUP
################################################################################
# Load all images
# imgPath = "images\Region_slope.1.jpg"
# img = mpimg.imread(imgPath)
# st.image(imgPath, width=None)

# Global Maps for introduction/informaiton/background
globalElevationPath = None
globalIlluminationPath = None
globalSlopePath = None
globalIceStabilityPath = None

# Individual zoomed maps for specific site
zoomedIlluminationPath = "images\zoomedIllumination.jpg"
zoomedIllumination = mpimg.imread(zoomedIlluminationPath)
zoomedSlopePath = "images\zoomedSlope.jpg"
zoomedSlope = mpimg.imread(zoomedSlopePath)
zoomedIceStabilityPath = "images\zoomedIceStability.jpg"
zoomedIceStability = mpimg.imread(zoomedIceStabilityPath)

# Combined viable terrain maps
globalViableIlluminationPath = "images\globalViableIllumination.jpg"
globalViableIllumination = mpimg.imread(globalViableIlluminationPath)
globalViableSlopePath = "images\globalViableSlope.jpg"
globalViableSlope = mpimg.imread(globalViableSlopePath)
globalViableCombinedPath = "images\globalViableCombined.jpg"
globalViableCombined = mpimg.imread(globalViableCombinedPath)

zoomedViableIlluminationPath = "images\zoomedViableIllumination.jpg"
zoomedViableIllumination = mpimg.imread(zoomedViableIlluminationPath)
zoomedViableSlopePath = "images\zoomedViableSlope.jpg"
zoomedViableSlope = mpimg.imread(zoomedViableSlopePath)
zoomedViableCombinedPath = "images\zoomedViableCombined.jpg"
zoomedViableCombined = mpimg.imread(zoomedViableCombinedPath)


################################################################################
# TEXT
################################################################################
# Title
title = 'Mission Planning'
description = 'Learn about lunar datasets, analyze landing sites, & design surface operations.'

# To describe each global map

# To describe combined maps
combinedDescription = '''Viable terrain means terrain traversible for a rover. 
    To achieve viable terrain, maps are filtered to fit rover contraints and ranked 
    as viable on a scale of 0 - 1, 0 being not viable at all, 1 being perfectly viable.
    The combined map shows total viable terrain. '''

# To desribe the purposes of each interactivity mechanism
# To walk user through the process
# To give historical background behind landing site analysis
# To explain what each map is


################################################################################
# DISPLAY
################################################################################
# title & description
st.title(title)
st.header(description)

# introduce lunar maps (note this might be broken into multiple tabs ****)
    # global elevation
    # global illumination over time
    # global slopes (all slopes? ****)
    # global ice stability at depth (all depth? ****)

allWidth = 700

st.subheader("Zoomed Lunar South Pole Maps")
row1a, row1b, row1c = st.beta_columns(3)    #images
row2a, row2b, row2c = st.beta_columns(3)    #titles
# global illumination over time
row1a.image(zoomedIllumination, width = allWidth)
row2a.write('Illumination Overtime')
# global slopes
row1b.image(zoomedSlope, width = allWidth)
row2b.write('Slopes')
# glbal ice stability at depth
row1c.image(zoomedIceStability, width = allWidth)
row2c.write('Ice Stability at Depth')

st.subheader("Viable Terrain Maps")
st.write(combinedDescription)
row3a, row3b, row3c = st.beta_columns(3)    #global images
row4a, row4b, row4c = st.beta_columns(3)    #zoomed images
# global combined maps
row3a.image(globalViableIllumination, width = allWidth)
row3a.write("Global Viable Illumination Overtime")
row3b.image(globalViableSlope, width = allWidth)
row3b.write("Global Viable Sloeps")
row3c.image(globalViableCombined, width = allWidth)
row3c.write("Global Viable Terrain Combined")
# zoomed combined maps
row4a.image(zoomedViableIllumination, width = allWidth)
row4a.write("Local Viable Illumination Overtime")
row4b.image(zoomedViableSlope, width = allWidth)
row4b.write("Local Viable Sloeps")
row4c.image(zoomedViableCombined, width = allWidth)
row4c.write("Local Viable Terrain Combined")


################################################################################
# INTERACTIVITY
################################################################################
# Select between maps of region: ice stability, slope, illumination over time
    # Users can single view each map
    # Users can change opacity between maps



# Combine maps to view viable terrain for slope and illumination:
    # Can select what makes viable terrain between slope and illumination
    # View shows slope, illumination, and combined in triad


# Detect craters
    # View shows elevation data of site
    # Users select crater size
    # Craters appear on map


# Waypoint selection & landing elipse
    # All maps users create can be added as layers to a view
    # User can filter in and out opacity
    # User can draw polygons on map 
    # User can draw waypoints on map
    # User can add landing location
    # User can add landing ellipse
    # User can number waypoints
    # User can store waypoints (sorted by number)

# High level rover path
    # User can toggle view of rover path between waypoints


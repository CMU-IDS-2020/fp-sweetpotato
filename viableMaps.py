# viable map view 
# LCS
# sweetpotato

import streamlit as st
from PIL import Image
# from main import savedImages

################################################################################
# DATA SETUP
################################################################################

# Global Individual
# globalV = global Viable, S = Slope, I = illumination, numbers = limits
globalV_S15 = Image.open("images/globalV_S15.jpg")
globalV_S25 = Image.open("images/globalV_S25.jpg")
globalV_S35 = Image.open("images/globalV_S35.jpg")

globalV_I70 = Image.open("images/globalV_I70.jpg")
globalV_I60 = Image.open("images/globalV_I60.jpg")
globalV_I50 = Image.open("images/globalV_I50.jpg")

# Global Combined
globalV_S15_I70 = Image.open("images/globalV_S15_I70.jpg")
globalV_S15_I60 = Image.open("images/globalV_S15_I60.jpg")
globalV_S15_I50 = Image.open("images/globalV_S15_I50.jpg")

globalV_S25_I70 = Image.open("images/globalV_S25_I70.jpg")
globalV_S25_I60 = Image.open("images/globalV_S25_I60.jpg")
globalV_S25_I50 = Image.open("images/globalV_S25_I50.jpg")

globalV_S35_I70 = Image.open("images/globalV_S35_I70.jpg")
globalV_S35_I60 = Image.open("images/globalV_S35_I60.jpg")
globalV_S35_I50 = Image.open("images/globalV_S35_I50.jpg")

# Local Individual
localV_S15 = Image.open("images/localV_S15.jpg")
localV_S25 = Image.open("images/localV_S25.jpg")
localV_S35 = Image.open("images/localV_S35.jpg")

localV_I70 = Image.open("images/localV_I70.jpg")
localV_I60 = Image.open("images/localV_I60.jpg")
localV_I50 = Image.open("images/localV_I50.jpg")

# Local Combined
localV_S15_I70 = Image.open("images/localV_S15_I70.jpg")
localV_S15_I60 = Image.open("images/localV_S15_I60.jpg")
localV_S15_I50 = Image.open("images/localV_S15_I50.jpg")

localV_S25_I70 = Image.open("images/localV_S25_I70.jpg")
localV_S25_I60 = Image.open("images/localV_S25_I60.jpg")
localV_S25_I50 = Image.open("images/localV_S25_I50.jpg")

localV_S35_I70 = Image.open("images/localV_S35_I70.jpg")
localV_S35_I60 = Image.open("images/localV_S35_I60.jpg")
localV_S35_I50 = Image.open("images/localV_S35_I50.jpg")

################################################################################
# MAP ORGANIZATION
################################################################################
# ALL LOCAL IMAGES
localSlopeImages = {0: localV_S15, 1: localV_S25, 2: localV_S35}
localIlluminationImages = {0: localV_I70, 1: localV_I60, 2: localV_I50}
# viable organized by {slopeScore: {illuminationScore:}}
localViable = {
    0:{0: localV_S15_I70, 1: localV_S15_I60, 2: localV_S15_I50},
    1:{0: localV_S25_I70, 1: localV_S25_I60, 2: localV_S25_I50},
    2:{0: localV_S35_I70, 1: localV_S35_I60, 2: localV_S35_I50}
}

# ALL GLOBAL IMAGES
globalSlopeImages = {0: globalV_S15, 1: globalV_S25, 2: globalV_S35}
globalIlluminationImages = {0: globalV_I70, 1: globalV_I60, 2: globalV_I50}
# viable organized by illuminationScore: {slopeScore:}
globalViable = {
    0:{0: globalV_S15_I70, 1: globalV_S15_I60, 2: globalV_S15_I50},
    1:{0: globalV_S25_I70, 1: globalV_S25_I60, 2: globalV_S25_I50},
    2:{0: globalV_S35_I70, 1: globalV_S35_I60, 2: globalV_S35_I50}
}

################################################################################
# VARIABLES & SUPPORTING FUNCTIONS
################################################################################

def displayLocal(illumination, slope, col1, col2):
    slopeImage = localSlopeImages[slope]
    illuminationImage = localIlluminationImages[illumination]
    viableImage = localViable[slope][illumination]
    col1.image(slopeImage, use_column_width = True)
    col2.image(illuminationImage, use_column_width = True)
    st.image(viableImage, use_column_width = True)

def displayGlobal(illumination, slope, col1, col2):
    slopeImage = globalSlopeImages[slope]
    illuminationImage = globalIlluminationImages[illumination]
    viableImage = globalViable[slope][illumination]
    col1.image(slopeImage, use_column_width = True)
    col2.image(illuminationImage, use_column_width = True)
    st.image(viableImage, use_column_width = True)

def addMaps(illumination, slope):
    slopeImage = localSlopeImages[slope]
    illuminationImage = localIlluminationImages[illumination]
    viableImage = localViable[slope][illumination]
    savedImages[f'Viable Slopes, risk: {slope}'] = slopeImage
    savedImages[f'Viable Illumination, risk: {illumination}'] = illuminationImage
    savedImages[f'Viable Slopes, risk: S{slope}, I{illumination}'] = viableImage

################################################################################
# MAIN RUN
################################################################################
def run():
    st.title("Configure Viable Terrain")
    st.write("** To view an image in full screen, hover over it and select the double arrows in the top right corner.")

    # ALL MAP SLIDERS
    st.sidebar.header('Slope')
    slope = st.sidebar.slider('Risk level (low to high)', 2, (0), key = 'Slope')
    st.sidebar.header('Illumination')
    illumination = st.sidebar.slider('Risk level (low to high)', 2, (0), key = 'Illumination')

    
    st.sidebar.header('View')
    globalView = st.sidebar.button('Global Maps')
    localView = st.sidebar.button('Local Maps')

    # CONFIGURE COLUMNS
    col1, col2 = st.beta_columns(2)

    # VIEWS
    if localView:
        displayLocal(illumination, slope, col1, col2)
    else:
        displayGlobal(illumination, slope, col1, col2)
    
    # SAVE MAPS FOR PLANNING
    #st.sidebar.text('------------------------')
    # st.sidebar.write('Export maps to operations planning tab')
    # wantToSave = st.sidebar.button('Save viable maps')
    # if wantToSave:
    #     addMaps(illumination, slope)
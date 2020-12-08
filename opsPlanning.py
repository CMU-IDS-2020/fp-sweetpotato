# ops planning
# LCS
# sweetpotato

# some source-code and references from:
# https://github.com/andfanilo/streamlit-drawable-canvas-demo/blob/master/app.py

import streamlit as st
from PIL import Image
import pandas as pd
import copy
from streamlit_drawable_canvas import st_canvas
################################################################################
# DATA SETUP
################################################################################

# Individual zoomed maps for specific site
localIllumination = Image.open("images/localIllumination.jpg")
localSlope = Image.open("images/localSlope.jpg")
localIceStability = Image.open("images/localIceStability.jpg")

# Background image options
images = {
    'Illumination': localIllumination,
    'Slope': localSlope,
    'Ice Stability': localIceStability
}

imageNames = list(images.keys())


################################################################################
# MAIN RUN
################################################################################
def run():
    # TITLE & INITIAL TEXT
    st.title("Operations Planning")
    st.set_option("deprecation.showfileUploaderEncoding", False)
    st.markdown(
        """
    Draw on the canvas, get the drawings back to Streamlit!
    * Doubleclick to remove the selected object when not in drawing mode
    """
    )

    # DRAWING TOOLS
    st.sidebar.header("Draw")
    drawing_mode = st.sidebar.selectbox(
        "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
    )
    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
    stroke_color = st.sidebar.beta_color_picker("Stroke color hex: ")

    # BACKGROUND IMAGES
    st.sidebar.header("Background Maps")
    op = st.sidebar.slider('Opacity', 100, (0), key = 'Layer 1')
    bgImageName = st.sidebar.selectbox("Select from local lunar maps", imageNames)
    bgImage = copy.copy(images[bgImageName])
    bgImage.putalpha(int(256*(op/100)))
    
    #bgImage = st.sidebar.file_uploader("Add background image:", type=["png", "jpg"])
    
    #realtimeUpdate = st.sidebar.checkbox("Update in realtime", True)

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_image= bgImage,
        #update_streamlit=realtimeUpdate,
        height=840,
        width=1120,
        drawing_mode=drawing_mode,
        key="canvas",
    )

    col1, col2 = st.beta_columns(2)
    col1 = canvas_result

    # Display stand alone diagrmas
    st.header('Diagram View')
    st.write('To view your drawn, stand-alone diagram, select the downward arrow in the lower right corner of the map above')

    # Do something interesting with the image data and paths
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data)
    # if canvas_result.json_data is not None:
    #     st.dataframe(pd.json_normalize(canvas_result.json_data["objects"]))

    

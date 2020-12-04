# IMAGE DATA
# LCS
# sweetpotato

import matplotlib.image as mpimg
from  PIL import Image

################################################################################
# DATA SETUP
################################################################################
# Load all images
# imgPath = "images\Region_slope.1.jpg"
# img = mpimg.imread(imgPath)
# st.image(imgPath, width=None)


# Initial TEST viable terrain maps
globalViableIllumination = Image.open("images/globalViableIllumination01.jpg")
globalViableSlope = Image.open("images/globalViableSlope01.jpg")
globalViableCombined = Image.open("images\globalViableCombined01.jpg")
localViableIllumination = Image.open("images\zoomedViableIllumination01.jpg")
localViableSlope = Image.open("images\zoomedViableSlope01.jpg")
localViableCombined = Image.open("images\zoomedViableCombined01.jpg")

#####

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

# Global Individual
# globalV = global Viable, S = Slope, I = illumination, numbers = limits
globalV_S15 = Image.open("images\globalV_S15.jpg")
globalV_S25 = Image.open("images\globalV_S25.jpg")
globalV_S35 = Image.open("images\globalV_S35.jpg")

globalV_I70 = Image.open("images\globalV_I70.jpg")
globalV_I60 = Image.open("images\globalV_I60.jpg")
globalV_I50 = Image.open("images\globalV_I50.jpg")

# Global Combined
globalV_S15_I70 = Image.open("images\globalV_S15_I70.jpg")
globalV_S15_I60 = Image.open("images\globalV_S15_I60.jpg")
globalV_S15_I50 = Image.open("images\globalV_S15_I50.jpg")

globalV_S25_I70 = Image.open("images\globalV_S25_I70.jpg")
globalV_S25_I60 = Image.open("images\globalV_S25_I60.jpg")
globalV_S25_I50 = Image.open("images\globalV_S25_I50.jpg")

globalV_S35_I70 = Image.open("images\globalV_S35_I70.jpg")
globalV_S35_I60 = Image.open("images\globalV_S35_I60.jpg")
globalV_S35_I50 = Image.open("images\globalV_S35_I50.jpg")

# Local Individual
localV_S15 = Image.open("images\localV_S15.jpg")
localV_S25 = Image.open("images\localV_S25.jpg")
localV_S35 = Image.open("images\localV_S35.jpg")

localV_I70 = Image.open("images\localV_I70.jpg")
localV_I60 = Image.open("images\localV_I60.jpg")
localV_I50 = Image.open("images\localV_I50.jpg")

# Local Combined
localV_S15_I70 = Image.open("images\localV_S15_I70.jpg")
localV_S15_I60 = Image.open("images\localV_S15_I60.jpg")
localV_S15_I50 = Image.open("images\localV_S15_I50.jpg")

localV_S25_I70 = Image.open("images\localV_S25_I70.jpg")
localV_S25_I60 = Image.open("images\localV_S25_I60.jpg")
localV_S25_I50 = Image.open("images\localV_S25_I50.jpg")

localV_S35_I70 = Image.open("images\localV_S35_I70.jpg")
localV_S35_I60 = Image.open("images\localV_S35_I60.jpg")
localV_S35_I50 = Image.open("images\localV_S35_I50.jpg")

# Tool for Lunar Polar Site Analysis

# 01 Introduction

**Site Analysis**

Site analysis is the process of understanding a planetary environment in order to prepare for a space mission. This analysis is conducted for both human and rover space exploration with the goals of understanding three core concepts --(a)  system capabilities for both rover/humans and lander, (b) science objectives, and (c) surrounding environmental conditions. Understanding a given site allows a mission to develop a more detailed Concept of Operations (CONOPs), specify surface operations, and design the rover or human exploration system around the environmental considerations that come with the environment during operations. This application is designed specifically for rover space exploration.

![A screenshot of three mission considerations.](writeUpImages/three_mission.jpg)

**Application Scope**

This application has four tabs. This is the Introduction to Site Analysis tab. The Individual Map View allows users to analyze specific datasets individually in a side-by-side and layered view. The Viable Terrain tab facilitates the configuration of viable terrain maps, customizable to riskier and less risky conditions relative to system capabilities. And finally an Operations Planning tab allows a user to manually draw on top of maps -- to configure surface operations, to outline regions of interest, or otherwise.

# 02 Related Work

Quite a few software tools exist supporting lunar site analysis. The table below details a list of these. The most relevant works are detailed further in the following paragraphs.


<table>
  <tr>
   <td><strong>Software</strong>
   </td>
   <td><strong>SIM</strong>
   </td>
   <td><strong>DEM</strong>
   </td>
   <td><strong>Data Analysis</strong>
   </td>
   <td><strong>Personalized</strong>
   </td>
   <td><strong>Available</strong>
   </td>
  </tr>
  <tr>
   <td>MATLAB
   </td>
   <td>✖
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
   <td>✔
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>MoonTrek
   </td>
   <td>✖
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>Gazebo
   </td>
   <td>✔
   </td>
   <td>✖
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
   <td>✔
   </td>
  </tr>
  <tr>
   <td>LunaRay
   </td>
   <td>✔
   </td>
   <td>✖
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
   <td><strong>?</strong>
   </td>
  </tr>
  <tr>
   <td>DEMkit
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
   <td><strong>?</strong>
   </td>
  </tr>
  <tr>
   <td>Lunar Polar Sim
   </td>
   <td>✔
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
   <td>✔
   </td>
   <td><strong>?</strong>
   </td>
  </tr>
  <tr>
   <td>Mars OnSight
   </td>
   <td>✖
   </td>
   <td>✔
   </td>
   <td>✖
   </td>
   <td>✖
   </td>
   <td><strong> ~ </strong>✔
   </td>
  </tr>
</table>


**Table 1. Table of existing software used in space mission contexts and their capabilities**

Table 1 lists multiple existing software tools and their capabilities to simulation the lunar environment (SIM), interact with a key data product - a digital elevation model (DEM), perform data analysis, allow for personalization (i.e. open source), and whether or not they are available for public. These each have their advantages, but none present a high fidelity capacity to address key surface operation analysis -- the ability to define and configure viable terrain maps for path planning purposes or to draw on specific surface operations.

![A screenshot of related work.](writeUpImages/relatedWork.jpg)
**Figure 2. Related work. A) Moontrek interface with ice stability data layered on top of slope data. B) Quickmap viewing crater names and Permanently Shadowed Regions. C) Mars OnSight. D) Lunar maps processed and visualized using Matlab.**

**MoonTrek** (fig. 2A) and **Quickmap** (fig 2B), are kind of like the photoshop of the space world, allowing a user to select a broad region of the Moon (north pole, south pole, equatorial region) and view datasets in 2D that are available in those locations. Resolution is low, and although opacity can be adjusted, it can be hard to understand the correlation between information. Datasets are selected as layers and cannot be combined for the purpose of constructing a viable terrain map.

**Mars OnSight** (fig. 2C) is a virtual reality environment constructed from stereo images collected by the Mars Curiosity rover. In this environment, scientists and mission personnel can enter and explore the environment. Interesting features can be tagged and some limited data can be associated with certain artefacts. This is only used, however, during the live surface operations of the rover and not during critical planning stages prior to launch. Full datasets of the environment cannot be viewed.

Finally, **Matlab** (fig. 2D) is a software commonly used within the math and engineering communities. This software program allows for extensive data analysis, but is not intuitive or easy to use for those unfamiliar.

The goals of this project are to leverage some existing successful capabilities of the aforementioned works and develop new functionality that fills the critical gaps of site analysis and surface operations planning.

# 03 Methods

P

used for this analysis were downloaded from the [Planetary Data Sciences Node](https://pds-geosciences.wustl.edu/lro/lro-l-lola-3-rdr-v1/lrolol_1xxx/data/lola_gdr/polar/jp2/#). 


# 04 Results


# 05 Discussion


# 06 Future Work


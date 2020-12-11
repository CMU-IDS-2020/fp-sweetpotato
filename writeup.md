# Tool for Lunar Polar Site Analysis

# 01 Introduction

**Site Analysis**

Site analysis is the process of understanding a planetary environment in order to prepare for a space mission. This analysis is conducted for both human and rover space exploration with the goals of understanding three core concepts --(a)  system capabilities for both rover/humans and lander, (b) science objectives, and (c) surrounding environmental conditions. Understanding a given site allows a mission to develop a more detailed Concept of Operations (CONOPs), specify surface operations, and design the rover or human exploration system around the environmental considerations that come with the environment during operations. This application is designed specifically for rover space exploration.

![A screenshot of three mission considerations.](writeupImages/three_mission.jpg)

**Application Scope**

This application has four tabs. This is the Introduction to Site Analysis tab. The Individual Map View allows users to analyze specific datasets individually in a side-by-side and layered view. The Viable Terrain tab facilitates the configuration of viable terrain maps, customizable to riskier and less risky conditions relative to system capabilities. And finally an Operations Planning tab allows a user to manually draw on top of maps -- to configure surface operations, to outline regions of interest, or otherwise.

# 02 Related Work

The complexity of space missions involves a conglomeration of knowledge and perspective from all mission aspects, ranging from mobility, visibility, and mechanical structures survival, to the scientific initiative purpose and landing location. Using software tools for data analysis often means breaking down these various information aspects piece-wise to try and understand the whole in a manual fashion. Furthermore, there exists the question of how specifically scientific initiative can be simulated. Usually, the mission’s Science Principle Investigator offers domain experience and direction to the team, leading them towards the scientific goals within the bounds of their capabilities. Some software tools exist to aid the process but none capture the essence of an individual’s personal perspective.


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

Table 1 lists multiple existing software tools and their capabilities to simulation the lunar environment (SIM), interact with a key data product - a digital elevation model (DEM), perform data analysis, allow for personalization (i.e. open source), and whether or not they are available for public or MoonRanger use. These each have their advantages, but none present a high fidelity capacity to address these questions. In the paragraphs to come the first three software tools are described in more detail.

![A screenshot of related work.](writeupImages/relatedWork.jpg)
**Figure 3. MoonTrek viewing LOLA Slope Data (in green) and Ice Stability at Depth Data (in red) [44]**

MoonTrek, the photoshop of the space world, allows a user to select a broad region of the Moon (north pole, south pole, equatorial region) and view datasets in 2D that are available in those locations. Resolution is low, and although opacity can be adjusted, it can be hard to understand the correlation between information.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.jpg "image_tooltip")


**Figure X. Quickmap interface. [45]**

Quickmap



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.jpg "image_tooltip")


**Figure 4. Gazebo, an existing software tool used to simulate mobile robots in an user-designed environment [43]**

Gazebo, one of the most commonly used tools for space simulation, is not a 2D environment for data analysis, but a simulation environment specifically for rover mobility and vision analysis. It is open-source, so allows a user to develop to their heart’s content the terrain, rover, and lighting specifications. However, it is incredibly non-intuitive, comes with a steep learning curve, and is good only for rover-scale simulation and not so much global planning.



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.jpg "image_tooltip")


**Figure 5. Plots of lunar datasets created using Matlab**

MATLAB, a software commonly used in the math and engineering communities, allows for extensive data analysis, but it doesn’t offer a sim environment.



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.jpg "image_tooltip")


**Figure 6. Image of the VR environment generated by Mars OnSight.**

Mars OnSight

Each of these aforementioned software environments presents various constraints technically speaking. In terms of development time, this work could easily take years and be a goal for a large team, resources permitting. However, as an individual with a years’ time to complete a thesis, a lean framework will be a feasible scope and is one that can inform future development. My current experimentation, research, and development has explored Gazebo and investigated LunaRay and DEMkit, but these tools don’t offer a robust platform for landing site analysis - a concept at the core of global planning. Matlab, while technical and simple, is a strong functional tool that will allow for landing site analysis and global planning and is the tool I have used most recently with the most success, with some intermediary analysis conducted in MoonTrek. With an algorithm structure and functionality to identify waypoints as a global planner, I plan to test the fidelity of the algorithm against manually analyzed landing sites, and then implement a version of the algorithm in a more user-intuitive and exploratory platform.


# 03 Methods

P

used for this analysis were downloaded from the [Planetary Data Sciences Node](https://pds-geosciences.wustl.edu/lro/lro-l-lola-3-rdr-v1/lrolol_1xxx/data/lola_gdr/polar/jp2/#). 


# 04 Results


# 05 Discussion


# 06 Future Work


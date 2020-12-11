# Tool for Lunar Polar Site Analysis

![A screenshot of macro view. Could be a GIF.](macroViewA3.jpg)
![A screenshot of individual view. Could be a GIF.](individualViewA3.jpg)

<!---[TODO: Short abstract describing the main goals and how you achieved them.]-->

## Introduction

**Site Analysis**\
Site analysis is the process of understanding a planetary environment in order to prepare for a space mission. This analysis is conducted for both human and rover space exploration with the goals of understanding three core concepts --(a)  system capabilities for both rover/humans and lander, (b) science objectives, and (c) surrounding environmental conditions. Understanding a given site allows a mission to develop a more detailed Concept of Operations (CONOPs), specify surface operations, and design the rover or human exploration system around the environmental considerations that come with the environment during operations. This application is designed specifically for rover space exploration.

**Application Scope**\
This application has four tabs. This is the Introduction to Site Analysis tab. The Individual Map View allows users to analyze specific datasets individually in a side-by-side and layered view. The Viable Terrain tab facilitates the configuration of viable terrain maps, customizable to riskier and less risky conditions relative to system capabilities. And finally an Operations Planning tab allows a user to manually draw on top of maps -- to configure surface operations, to outline regions of interest, or otherwise. Have fun and enjoy!

## Related Work

<!---[TODO: **A clear description of the goals of your project.** Describe the question that you are enabling a user to answer. The question should be compelling and the solution should be focused on helping users achieve their goals. ]-->

Our project goals are twofold. We want to provide a tool for both a higher-level and lower-level look at restaurant data. For a business owner or city planner, the first question **(Q1)** is 'how have prefernce sentiment (negative, positive, or neutral) changed overtime and how do these vary between cities?' For a general user, the second question **(Q2)** is 'how can a restaurant search be configured to an in individual's taste and preferences?'

## Design

<!---[TODO: **A rationale for your design decisions.** How did you choose your particular visual encodings and interaction techniques? What alternatives did you consider and how did you arrive at your ultimate choices?]-->

Note that we transformed all reviews in these four cities into one of three sentiments - positive, neutral and negative - using [VADER](https://www.thepythoncode.com/article/vaderSentiment-tool-to-extract-sentimental-values-in-texts-using-python).

**TAB 1**: Macro-City View\
To address **Q1**, we created a viewport allowing a user to view four maps. Maps show restaurant data for Pittsburgh, Montreal, Cleveland, and Toronto. Users can specify a range of stars (1 to 5) with which to filter the data. Maps update to show all restaurants within that star range. A graph below shows how negative, positive, and neutral preference has changed overtime. Users can select select between three buttons ('Negative,' 'Positive,' and 'Neutral') to specify a the sentement of reviews and ratings. The chart updates, colorizing the degree of negativity/positivity/neutrality over each year of submitted reviews to reflect the strength of sentiment. The size of each circle on the graph remains the same and showcases the total number or reviews submitted over time for each. In this view users cannot see the specific data of each city to reduce the over-saturation of information and keep the focus around restaurant sentiment. Users can also view their selected preference modeled as average sentiment over time, combining reviews from all cities.

**TAB 2**: Individual View\
**Q2** is addressed in a second view port. The visuals here focus on just one city at a time, allowing users to zero in on more detailed city data without being overwhelmed by information. This view allows users to select one of the four cities, see the top 10 restaurants, and show view based on review count or stars. Users can filter the map to show a range of stars and price range, and use drop downs to apply filters for restaurant characteristics and zip code. For example, if one wants to find a _classy_ restaurant that plays _jazz_ music and provides a free _WIFI_ in _her neighborhood_ (as in the same zip code), no problem! She could easily select these filters and sort by either stars or review count to select the restaurant for her night. We also provide temporal trends of positive/neutral/negative sentiment for each restaurant if you simply type one of their names. Say, you are a restaurant owner who wants to know how to improve your Yelp rating. We provide a Yelp star prediction based on the change in sentiment. For example, one can easily see how ratings change based on the change in sentiment value per restaurant. 

## Development

<!---[TODO: **An overview of your development process.** Describe how the work was split among the team members. Include a commentary on the development process, including answers to the following questions: Roughly how much time did you spend developing your application (in people-hours)? What aspects took the most time?]-->

The development process developed within several stages articulated below. Total development time took roughly 92 hours total. Figuring out Streamlit, between understanding its processing power, speed, abilities, configuration, and ability to interface with Altair, took the most time at maybe 50%. Debugging came in second for time consumption at around 30%, with the integration process taking maybe 20%.

**Planning & Testing Options**\
The development process begain in the planning phase in which we considered our interests, questions, and possible topics. These included the following:

Space Focus: Exoplanet or solar-system data were the fist considerations. We investigated the datasets available and the existing libraries that could help our development. Datasets on exoplanets were available, but because not all data properties were available consistently and no substantial libraries exist for space-specific data, we determined this was not the right path. We estimated the manual processes we would need to perform would overpower our visuaization and machine learning focus with streamlit. Lydia investigated datasets. We both investigated space libraries.

Art Focus: Next, we considered the option of an art-focussed project. We decided to combine solar system data into this project idea. NASA JPL released a poster series entitled "Exoplanet Travel Bureau." This poster series consists of human-drawn renderings of the worlds that humans could encounter at a figurative level on planets outside of our solar system. Posters show terrain colored by a red sun, or multiple planets in the sky all correlating to the data behind each exoplanet but artistically rendered to transport a viewer to the exoplanet realm. Our plan was to use a machine learning method to transform classically historic paintings using the visual characteristics of planets in our solar system. However, the machine learning process took too long to load on Streamlit, so we moved on. Clay implemented the machine learning to test on Streamlit and Lydia organized planet images and designed interactivity methods.

We both met often and discussed throughout this process testing out each option thoroughly.

**Topic Selection & Intermediate Steps**\
Yelp Focus: This focus, our ultimate choice, was a dataset easily structured and provided detailed characteristics about businesses and reviews. We figured we could use this well documented and organized data to build powerful visuals dedicated to spacific user goals.

Intermediate steps involved designing an interface, parsing and organizing data, and figuring out the Streamlit development platform. Clay parsed and organized the data, Lydia developed intial sketches of visualization interface, and we both investigated the Streamlit visualization platform.

![A screenshot of visualization interface sketch. Could be a GIF.](interfaceSketchA3.jpg)

**Individual Development**\
Now we defined our individual development. Clay focussed on the individual viewport with machine learning and Lydia focussed on the macro scale view port with Altair. We both met frequently to discuss progress, ideas, and direction.

**Combination & Conclusion**\
The final process involved combining our code. We both pushed our code to the Github repository and Clay integrated the code. Lydia wrote the writeup. Throughout this process, we met frequently to test the integration, and discuss design changes.

## TEST HERE

Table of Contents


[TOC]



# 01 Introduction

**Site Analysis**

Site analysis is the process of understanding a planetary environment in order to prepare for a space mission. This analysis is conducted for both human and rover space exploration with the goals of understanding three core concepts --(a)  system capabilities for both rover/humans and lander, (b) science objectives, and (c) surrounding environmental conditions. Understanding a given site allows a mission to develop a more detailed Concept of Operations (CONOPs), specify surface operations, and design the rover or human exploration system around the environmental considerations that come with the environment during operations. This application is designed specifically for rover space exploration.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.jpg "image_tooltip")


**Application Scope**

This application has four tabs. This is the Introduction to Site Analysis tab. The Individual Map View allows users to analyze specific datasets individually in a side-by-side and layered view. The Viable Terrain tab facilitates the configuration of viable terrain maps, customizable to riskier and less risky conditions relative to system capabilities. And finally an Operations Planning tab allows a user to manually draw on top of maps -- to configure surface operations, to outline regions of interest, or otherwise. Have fun and enjoy!


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



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.jpg "image_tooltip")


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


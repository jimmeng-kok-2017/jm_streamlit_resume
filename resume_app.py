import streamlit as st
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from streamlit_echarts import st_echarts
import os
import json
import requests
from streamlit_folium import folium_static
import folium


# st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Kok Jim Meng
##### *Resume*
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Motivated Learner, and have a passion for analytics by developing analytics products and delivering insights by writing articles. 
- Strong relevant analytics experience from Urban Redevelopment Authority (URA), Changi General Hospital (CGH), and Ernst and Young (EY).
- Reading, understanding, and catching up with the up and coming analytics & machine learning libraries through self-learning during free time. 
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #70A1FF;">
  <a class="navbar-brand" href="https://jimintheworld.medium.com/" target="_blank">Kok Jim Meng</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#academic-projects">Academic Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#streamlit-applications">Streamlit Applications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
# F0FF5F

# <li class="nav-item">
#         <a class="nav-link" href="#streamlit-projects">Streamlit Applications</a>
#       </li>

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([3,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([3,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
##### Map showing the location of my Academic and Work Experience
''')

tp_string = 'https://developers.onemap.sg/commonapi/search?searchVal='+'Temasek Polytechnic'+'&returnGeom=Y&getAddrDetails=Y'
tp_resp = requests.get(tp_string)
tp_data = json.loads(tp_resp.content)
tp_real_data = tp_data['results'][0]
tp_lat = float(tp_real_data['LATITUDE'])
tp_long = float(tp_real_data['LONGITUDE'])

smu_string = 'https://developers.onemap.sg/commonapi/search?searchVal='+'Singapore Management University'+'&returnGeom=Y&getAddrDetails=Y'
smu_resp = requests.get(smu_string)
smu_data = json.loads(smu_resp.content)
smu_real_data = smu_data['results'][6]
smu_lat = float(smu_real_data['LATITUDE'])
smu_long = float(smu_real_data['LONGITUDE'])

dhl_string = 'https://developers.onemap.sg/commonapi/search?searchVal='+'DHL EXPRESS SOUTH EAST ASIA HUB'+'&returnGeom=Y&getAddrDetails=Y'
dhl_resp = requests.get(dhl_string)
dhl_data = json.loads(dhl_resp.content)
dhl_real_data = dhl_data['results'][0]
dhl_lat = float(dhl_real_data['LATITUDE'])
dhl_long = float(dhl_real_data['LONGITUDE'])

cgh_string = 'https://developers.onemap.sg/commonapi/search?searchVal='+'Changi General Hospital'+'&returnGeom=Y&getAddrDetails=Y'
cgh_resp = requests.get(cgh_string)
cgh_data = json.loads(cgh_resp.content)
cgh_real_data = cgh_data['results'][0]
cgh_lat = float(cgh_real_data['LATITUDE'])
cgh_long = float(cgh_real_data['LONGITUDE'])

ura_string = 'https://developers.onemap.sg/commonapi/search?searchVal='+'Urban Redevelopment Authority'+'&returnGeom=Y&getAddrDetails=Y'
ura_resp = requests.get(ura_string)
ura_data = json.loads(ura_resp.content)
ura_real_data = ura_data['results'][0]
ura_lat = float(ura_real_data['LATITUDE'])
ura_long = float(ura_real_data['LONGITUDE'])

deloitte_lat = 1.279294354726619
deloitte_long = 103.8492895

ey_lat = 1.2823211397542482
ey_long = 103.85174512329272

m = folium.Map(location=[1.3627228720885567, 103.80849927659521], zoom_start=11)

folium.Marker(location=[tp_lat,tp_long], popup='Temasek Polytechnic: 2012-2015',icon=folium.Icon(icon="graduation-cap", prefix='fa')).add_to(m)
folium.Marker(location=[smu_lat,smu_long], popup='Singapore Management University: 2017-2021',icon=folium.Icon(icon="graduation-cap", prefix='fa')).add_to(m)
folium.Marker(location=[deloitte_lat,deloitte_long], popup='Deloitte: 2014',icon=folium.Icon(icon="laptop", prefix='fa')).add_to(m)
folium.Marker(location=[dhl_lat,dhl_long], popup='DHL Express: 2019',icon=folium.Icon(icon="laptop", prefix='fa')).add_to(m)
folium.Marker(location=[ura_lat,ura_long], popup='Urban Redevelopment Authority: 2021',icon=folium.Icon(icon="laptop", prefix='fa')).add_to(m)
folium.Marker(location=[ey_lat,ey_long], popup='Ernst and Young: 2021',icon=folium.Icon(icon="laptop", prefix='fa')).add_to(m)
folium.Marker(location=[cgh_lat,cgh_long], popup='Changi General Hospital: 2022-Present',icon=folium.Icon(icon="laptop", prefix='fa')).add_to(m)

folium_static(m)

#####################
st.markdown('''
## Education
''')

txt('**Bachelor of Science** (Information Systems: Business Analytics), *Singapore Management University*, Singapore',
'2017-2021')
st.markdown('''
- Relevant Coursework: `Geographic Information Systems for Urban Planning`, `Text Mining and Language Processing`, `Visual Analytics for Business Intelligence`, `Data Analytics and Visualization for Communication Management`, `Social Analytics and Applications`
''')

txt('**Diploma** (Business Information Technology), *Temasek Polytechnic*, Singapore',
'2012-2015')
st.markdown('''
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Management Analyst**, Changi General Hospital, Singapore',
'Jan 2022-Present')
st.markdown('''
- Preparing `2` regulatory reports to the Ministry of Health (MOH) and SingHealth on a daily basis regarding the operational situation of the hospital, bed occupancy rate, and inflight Covid-19 cases through database platforms including Oracle Business Intelligence Enterprise Edition (OBIEE) and SAP. 
- Deliver Quality Incentive KPIs reporting in Tableau of `300+` medical discipline specialists across the hospital to the Medical Affairs monthly.
- Performing complex data analysis and investigation on `600+` discharged patients' data through SAP and Sunrise Clinical Manager (SCM) for accurate reporting.
''')

txt('**Business Analyst**, Ernst and Young, Singapore',
'Sep 2021-Nov 2021')
st.markdown('''
- Conducted data extraction for reporting and analysis to support `30+` ticket troubleshooting and stakeholders’ requests by executing SQL scripts in SQL Server Management Studio databases.
- Analysed insights on the `7` system utilisations of the client’s application through AWS CloudWatch dashboard reporting.
''')

txt('**Geospatial & Data Science Intern**, Urban Redevelopment Authority, Singapore',
'Jan 2021-Jul 2021')
st.markdown('''
- Conducted trends analysis and explored time-series clustering in `20+` carparks to better understand how land-use affects the parking occupancy patterns.
- Developed a trained named-entity recognition (NER) model that is mainly for location entities by leveraging spaCy in terms of the names of the local places and addresses, identified textual location references from unstructured text to geolocate spatial references from `800+` of unstructured textual input.
- Assembled `40+` years of historical land-use data through cleaning and geoprocessing spatial datasets in ArcGIS and conducted visualisations of the results using Python to identify insights among the trends analysis.
- Analysed footfall patterns in `2` hawker centres to gain meaningful insights in guiding the siting of future hawker centres.
''')

txt('**IT Intern**, DHL Express, Singapore',
'Apr 2019-Aug 2019')
st.markdown('''
- Collaborated with the Customs Clearance team including identifying and defining requirements, and analysing the feasibility of existing declaration processes for RPA
- Created a detailed Process Definition Document, which was well-received by the management and was used in a multi-regional RPA meeting for the company.
- Built a successful RPA project of transferring data from Outlook to the customs declaration portal to assist the Customs Clearance team via UiPath Studio, resulting in improving accuracy and reducing both `75%` of man-hours and manual customs declaration errors.
- Created a live-action simulation video to raise awareness and advocate the importance of IT security to all the employees of DHL Express South Asia Hub.
''')

txt('**Data Analyst Intern**, Deloitte, Singapore',
'Apr 2014-Aug 2014')
st.markdown('''
- Imported, exported, and manipulated a high volume of datasets by using Microsoft SQL Server.
- Collaborated with the data visualisation team closely when selecting the appropriate visualizations for BI deliverables.
- Developed `3` client interactive visualisation dashboards to drive key business decisions via Tableau.
''')

#####################
st.markdown('''
## Academic Projects
''')
txt4('Analysing IMDb Movies Ratings (Data Analytics and Visualisation for Communication Management)', 'A Data Analytics Project that focuses on discovering insights and significance based on the relationships between ratings and the different factors of the movies such as year, duration, and genre of the movies by communicate and visualise insights through visualisations and models such as ANOVA and Multiple Linear Regression', 'https://movieanalytics.netlify.app/')
txt4('Information Extraction of COVID-19 Research Papers (Text Mining and Language Processing)', 'A Text Mining & Language Processing Project that focuses on the extraction of COVID-19 information through scientific papers by leveraging text mining techniques such as Topic Modelling to Document Clustering to save the scientists\' time in getting information about COVID-19 through understanding the relevant themes of the scientific papers through the means of both Topic Modelling and Document Clustering.', 'https://youtu.be/rTOzHdSDWZM')
txt4('Business Profiling (Geographic Information Systems for Urban Planning)', 'A Geographic Information System Project that focuses on the theme of business profiling to strategise and analyse on the trade areas and business profile of the 13 International Food & Beverage outlets based in Taiwan. The project is aimed to analyse on how the point-of-interests can affect the outlets\' sales performance. Recommendations are provided to assist the International Food & Beverage company in understanding their market positioning against their competitors','https://wiki.smu.edu.sg/1920t1smt201/G1-Group08_Proposal')
txt4('Visualising Global Terrorism Act (Visual Analytics for Business Intelligence)', 'A Business Intelligence Project that focuses on communicating and visualising overall insight on the frequency and spread of global terrorism acts between 2002 to 2017 in different regions, their relationship with the development status of the countries affected, and the terrorist groups’ implications of the attacks', 'https://wiki.smu.edu.sg/1920t1is428g1/Task_Force_428:_Proposal')
txt4('Food Influencer Recommender (Social Analytics and Applications)', 'A Social Analytics Project that focuses on making personalised recommendations on trending food for businesses to sell, and relevant influencers to engage in promoting their businesses and food due to the Covid-19 pandemic that affects the F&B businesses.','https://towardsdatascience.com/foodiebuddie-how-we-built-singapores-first-food-recommender-b7f3eed0ac77')

st.markdown('''
## Streamlit Applications
''')
txt3('Vaccination Center Finder App','https://share.streamlit.io/jimmeng-kok-2017/choose_vaccines_sg/app.py')
txt3('Real-Time Weather Forecasting App','https://share.streamlit.io/jimmeng-kok-2017/weather_forecasting_app/main/main_app.py')
txt3('Shark Attack Survival Predictor App','https://share.streamlit.io/jimmeng-kok-2017/shark_attack/main/app.py')


#####################
st.markdown('''
## Skills
''')
txt3('Programming:', '`Python`, `R`')
txt3('Data Processing/Wrangling:', '`SQL`, `Pandas`, `Numpy`')
txt3('Data Visualisation:', '`Matplotlib`, `Seaborn`, `Plotly`, `ggplot2`, `Dash`, `R flexdashboard`, `Tableau`, `QGIS`')
txt3('Machine Learning:', '`scikit-learn`, `SHAP`, `PyCaret`')
txt3('Model Deployment:', '`Streamlit`, `R Shiny`')
txt3('Content Creation:', '`Adobe Premiere Pro`')

chart1,chart2 = st.columns(2)

with chart1:
    st.markdown("**Proficiency level of my Coding Languages (%)**")

    coding_options = {
      "tooltip": {
        "trigger": 'item'
      },
      "legend": {
        "top": '5%',
        "left": 'center'
      },
      "series": [
        {
          "name": 'Coding Language',
          "type": 'pie',
          "radius": ['40%', '70%'],
          "avoidLabelOverlap": "false",
          "itemStyle": {
            "borderRadius": 10,
            "borderColor": '#fff',
            "borderWidth": 2
          },
          "label": {
            "show": "false",
            "position": 'center'
          },
          "emphasis": {
            "label": {
              "show": "true",
              "fontSize": '40',
              "fontWeight": 'bold'
            }
          },
          "labelLine": {
            "show": "false"
          },
          "data": [
            { "value": 36, "name": 'Python' },
            { "value": 32, "name": 'R' },
            { "value": 32, "name": 'SQL' }
          ]
        }
      ]
    }
    st_echarts(options=coding_options, width="100%", key=0)

with chart2:
    st.markdown("**Skills that I have acquired (%)**")

    skills_options = {
      "tooltip": {
        "trigger": 'item'
      },
      "legend": {
        "top": '5%',
        "left": 'center'
      },
      "series": [
        {
          "name": 'Skills',
          "type": 'pie',
          "radius": ['40%', '70%'],
          "avoidLabelOverlap": "false",
          "itemStyle": {
            "borderRadius": 10,
            "borderColor": '#fff',
            "borderWidth": 2
          },
          "label": {
            "show": "false",
            "position": 'center'
          },
          "emphasis": {
            "label": {
              "show": "true",
              "fontSize": '40',
              "fontWeight": 'bold'
            }
          },
          "labelLine": {
            "show": "false"
          },
          "data": [
            { "value": 40, "name": 'Data Science and Analytics' },
            { "value": 35, "name": 'Machine Learning' },
            { "value": 25, "name": 'Marketing & Communications' }
          ]
        }
      ]
    }
    st_echarts(options=skills_options, width="100%", key=1)

# # Make accurate % in seaborn pie plt
# def make_autopct(values):
#   def my_autopct(pct):
#     return '{p:.0f}%'.format(p=pct)
#   return my_autopct

# coding_colors = sns.color_palette('pastel')
# coding_picked_colors = coding_colors[0:2]
# coding_percentage = [32,32,36]
# coding_attributes = ['SQL', 'R', 'Python']
# fig1 = plt.figure(figsize = (5,5))
# plt.pie(coding_percentage,labels=coding_attributes, explode = [0.1,0.1,0.1], autopct=make_autopct(coding_percentage), colors=coding_colors,textprops={'fontsize': 10, 'color':'black', 'weight':'bold'})

# skills_colors = sns.color_palette('pastel')
# skills_picked_colors = skills_colors[0:2]
# skills_percentage = [25,35,40]
# skills_attributes = ['Marketing & Communications', 'Machine Learning', 'Data Science and Analytics']
# fig2 = plt.figure(figsize = (5,5))
# plt.pie(skills_percentage,labels=skills_attributes, explode = [0.1,0.1,0.1], autopct=make_autopct(skills_percentage), colors=skills_colors,textprops={'fontsize': 20, 'color':'black', 'weight':'bold'})

# st.pyplot(fig1)

# st.pyplot(fig2)

st.markdown("**Ideal Candidate\'s Requirements**")
table1 = go.Figure(data=[go.Table(header=dict(values=['Your potential candidate has', 'Am I your ideal candidate?']),
                               cells=dict(values=[['Able to extract data from multiple sources',
     'Bond well with the team and motivated learner and hard worker',
     'Good Communication Skills to deliver insights and recommendations',
     'Strong knowledge of Python\'s and R\'s Analytics & Machine Learning Libraries as well as Tableau',
     'At least 5 years of working experience in analytics',
     'Experience in leading data analytics projects'],['Yes','Yes','Yes','Yes',
     'No, but I do have experience in analytics since 2019 whereby I have experienced in building different projects from academic projects to working on my personal side projects which helped me secure my internship at URA through publishing articles on Towards Data Science amidst the Covid-19 pandemic.',
     'No, but I did lead a team of 3 people, including me, in the Geospatial Analytics project which helped to achieve a distinction in the module back in SMU. Furthermore, I am eager to learn and motivate myself to acquire analytics work experience to lead my path to the day where I can able to lead a data analytics project and acquire project management skills at the same time.']]))
                      ]).update_layout(height=575)
st.plotly_chart(table1)

# def showchart(a, b):
#   col1, col2 = st.beta_columns([3,2])
#   with col1:
#     st.markdown(a)
#   with col2:
#     st.pyplot(b, use_container_width=True)
#
# def showtable(a, b):
#   col1, col2 = st.beta_columns([3,2])
#   with col1:
#     st.markdown(a)
#   with col2:
#     st.plotly_chart(b)

# title1,chart1 = st.beta_columns([2,2])
# title2,chart2 = st.beta_columns([2,2])
# title3,chart3 = st.beta_columns([2,2])

# with title1:
#   st.markdown("<h5 style='text-align: center;'>Proficiency level of my Coding Languages</h5>", unsafe_allow_html=True)
#
# with title2:
#   st.markdown("<h5 style='text-align: center;'>Skills that I have acquired</h5>", unsafe_allow_html=True)
#
# with title3:
#   st.markdown("<h5 style='text-align: center;'>Ideal Candidate\'s Requirements</h5>", unsafe_allow_html=True)

# with chart1:
#   coding_colors = sns.color_palette('pastel')
#   coding_picked_colors = coding_colors[0:2]
#   coding_percentage = [32,32,36]
#   coding_attributes = ['SQL', 'R', 'Python']
#   fig1 = plt.figure(figsize = (5,5))
#   plt.pie(coding_percentage,labels=coding_attributes, explode = [0.1,0.1,0.1], autopct='%i%%', colors=coding_colors,textprops={'fontsize': 20, 'color':'black', 'weight':'bold'})
#   st.pyplot(fig1, use_container_width=True)

# with chart2:
#   skills_colors = sns.color_palette('pastel')
#   skills_picked_colors = skills_colors[0:2]
#   skills_percentage = [25,35,40]
#   skills_attributes = ['Marketing & Communications', 'Machine Learning', 'Data Science and Analytics']
#   fig2 = plt.figure(figsize = (5,5))
#   plt.pie(skills_percentage,labels=skills_attributes, explode = [0.1,0.1,0.1], autopct='%i%%', colors=skills_colors,textprops={'fontsize': 20, 'color':'black', 'weight':'bold'})
#   st.pyplot(fig2, use_container_width=True)
#
# with chart3:
  # X = ['Able to extract data from multiple sources',
  #      'Bond well with the team and motivated learner and hard worker',
  #      'Good Communication Skills to deliver insights and recommendations',
  #      'Strong knowledge of Python\'s and R\'s Analytics & Machine Learning Libraries as well as Tableau',
  #      'At least 5 years of working experience in analytics',
  #      'Experience in leading data analytics projects']
  # Y = ['Yes','Yes','Yes','Yes',
  #      'No, but I do have experience in analytics since 2019 regardless it\'s during work, academic period, or working side projects as hobbies',
  #      'No, but I did lead one of my academic projects on Geospatial Analytics back in SMU. Furthermore, I am eager to learn and motivate myself to acquire analytics work experience to lead my path to the day where I can able to lead a data analytics project and acquire project management skills at the same time']
  # hire_me_data = pd.DataFrame([X,Y]).T
  # hire_me_data.columns = ['Your potential candidate has', 'Am I your ideal candidate?']
  # st.dataframe(hire_me_data,500)

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/jimmengkok')
txt2('GitHub', 'https://github.com/jimmeng-kok-2017/')
txt2('Towards Data Science', 'http://towardsdatascience.com/@jimintheworld')

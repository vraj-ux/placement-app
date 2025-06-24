# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 11:33:26 2025

@author: Vraj
"""


import pickle
import streamlit as st

# Load models
weather_classification = pickle.load(open("C:/Users/Yash/OneDrive/Desktop/Weather Classification/weather_data.sav", 'rb'))

# Diabetes Prediction

st.title('Weather Classification using ML')
col1, col2, col3 = st.columns(3)

with col1:
    temperature = st.text_input('Enter number of Temperature :', '31')
with col2:
    Humidity = st.text_input('Enter Humidity:', '74')
with col3:
    wind = st.text_input('Enter Wind Speed:', '14')
with col1:
    percipitation = st.text_input('Enter Percipitation:', '73')
with col2:
    cloud_cover = st.text_input('Enter Cloud Cover(overcast:0, Party cloudy:1, clear = 2, cloudy:3):', '3')
with col3:
    atmosphere = st.text_input('Atmosphere:', '998')
with col1:
    uv = st.text_input('UV index:', '3')
with col2:
    season = st.text_input('Enter season(winter :0, Spring :1, autumn: 2, Summer:3):', '2')
with col3:
    visibility = st.text_input('Enter Visibility:', '11')
with col3:
    location = st.text_input('Enter Location type(Inland: 0, Mountain: 1,Coastal: 2):', '2')
    
weather_type = ''
if st.button('Wether Type Result'):
    try:
        weather_prediction = weather_classification.predict([[
            int(temperature), int(Humidity), float(wind),
            int(percipitation),int(cloud_cover), float(atmosphere), int(uv),
            int(season), float(visibility), int(location)
        ]])
        if(weather_prediction[0]==0):
            weather_type ="Rainy"
        elif(weather_prediction[0]==1):
            weather_type ="Sunny"
        elif(weather_prediction[0]==2):
            weather_type ="Overcast"
        elif(weather_prediction[0]==3):
            weather_type ="Cloudy"
        elif(weather_prediction[0]==4):
            weather_type = "Snowy "
          
    except Exception as e:
        st.error(f"Error during prediction: {e}")

st.success(weather_type)

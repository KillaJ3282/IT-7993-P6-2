import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    layout="wide", 
    page_title='KSU RSS Feed Parser • Home',
    page_icon='📰'
)

add_logo('ksu_logo_resized.png')

st.title('Welcome to our RSS Feed Parser!')

st.write('This application is used for a quick parse across financial headlines and employs an AI sentiment analysis procedure against this data. While there are a good number of sources already within the dataset, you have the ability to upload custom sources for analysis - use the "Refresh Sources" option to use this. For an analysis of what has already been stored simply use the "Analyze Sources" option and select your keywords and data range to analyze. We hope this will enable you to see the general sentiment of the market - happy analyzing!, ')

st.subheader('By: Raissa Divinagracia, Ryan Griffin, Justin Mayercik, Joshua McMillion, and Jacob Sweat')

import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    layout="wide", 
    page_title='KSU RSS Feed Parser • Home',
    page_icon='📰'
)

add_logo('ksu_logo_resized.png')

st.title('Welcome to our RSS Financial News Feed Parser!')

st.write('This application will ')

st.subheader('By: Raissa Divinagracia, Ryan Griffin, Justin Mayercik, Joshua McMillion, and Jacob Sweat')
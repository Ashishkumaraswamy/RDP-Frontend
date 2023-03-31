# Libraries
import streamlit as st
import pandas as pd

# Config
st.set_page_config(page_title='Recruitment Data Platform',
                   page_icon=':bar_chart:', layout='wide')

st.markdown("<h1 style='text-align: center; color: #014b94 ;font-size:50px'>RECRUITMENT DATA PLATFORM</h1><hr>",
            unsafe_allow_html=True)
# Style
with open('frontend\style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title('Recruitment Data Platform')
st.markdown("<hr>", unsafe_allow_html=True)

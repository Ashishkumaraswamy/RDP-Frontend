# Libraries
import streamlit as st
import pandas as pd

# Config
st.set_page_config(page_title='Recruitment Data Platform',
                   page_icon=':bar_chart:', layout='wide')

st.markdown("<h1 style='text-align: center; color: #014b94 ;font-size:50px'>RECRUITMENT DATA PLATFORM</h1><hr>",
            unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #014b94 ;font-size:30px'>TEAM MEMBERS</h2><hr>",
            unsafe_allow_html=True)

team_members = {'Roll No':['19PD06','19PD07','19PD21','19PD22','19PD27'], 'Name':['Ashish K','Bala Vignesh SM','Maadhav K','Mohammed Hafiz','Hariharan S']}
team_members = pd.DataFrame(team_members)
st.table(team_members)


# Libraries
import streamlit as st
import requests
from datetime import datetime

# Config
st.set_page_config(page_title='Recruitment Data Platform',
                   page_icon=':bar_chart:', layout='wide')

st.markdown("<h1 style='text-align: center; color: #014b94 ;font-size:50px'>RECRUITMENT DATA PLATFORM</h1>",
            unsafe_allow_html=True)
# Style
with open('frontend\style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def fetch_all_jobs():
    resp = requests.get(
        'https://cc-lab-rdp.azurewebsites.net/jobs')
    jobs_all = resp.json()
    return jobs_all


def fetch_employee_details(eid):
    headers = {"Content-type": "application/json"}
    data = {"id": eid}
    print(data)
    resp = requests.post(
        "https://employee-data-platform.vercel.app/api/fetchone", json=data)
    if resp.status_code == 400:
        print('Error 400')
    else:
        print(resp.json())
        return resp.json()


def delete(job_id):
    global jobs_all
    resp = requests.delete(
        "https://cc-lab-rdp.azurewebsites.net/jobs/delete/"+str(job_id))
    print(resp.text)
    st.experimental_rerun()


def display_job(job):
    print("job info", job)

    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(
        [3, 4, 4, 3, 4, 3, 3, 3])
    with c1:
        st.markdown(
            "<p style='text-align: center;'>{}</p>".format(job["jobTitle"]), unsafe_allow_html=True)
    with c2:
        st.markdown(
            "<p style='text-align: center;'>{}</p>".format(job["jobDescription"]), unsafe_allow_html=True)
    with c3:
        st.markdown(
            "<p style='text-align: center;'>{}</p>".format(job["requirements"]), unsafe_allow_html=True)
    with c4:
        st.markdown(
            "<p style='text-align: center;'>{}</p>".format(job["isOpen"]), unsafe_allow_html=True)
    with c5:
        st.markdown(
            "<p style='text-align: center;'>{}</p>".format(job["lastDateToApply"]), unsafe_allow_html=True)
    with c6:
        st.markdown(
            "<p style='text-align: center;'>{}</p>".format(job["salary"]), unsafe_allow_html=True)
    with c7:
        employee_data = fetch_employee_details(job["postedBy"])
        st.markdown(
            "<p style='text-align: center;'>{}</p>".format(employee_data[0]["first_name"]), unsafe_allow_html=True)
    with c8:
        if st.button('Delete Job', type="primary", key=job["jobId"]):
            delete(job_id=job['jobId'])


def display_all_jobs():
    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(
        [3, 4, 4, 3, 4, 3, 3, 3])
    with c1:
        st.markdown(
            f"<h2 style='text-align: center; font-size: 20px;'>Job Title</h2>", unsafe_allow_html=True)
    with c2:
        st.markdown(
            f"<h2 style='text-align: center; font-size: 20px;'>Job Description</h2>", unsafe_allow_html=True)
    with c3:
        st.markdown(
            f"<h2 style='text-align: center; font-size: 20px;'>Requirements</h2>", unsafe_allow_html=True)
    with c4:
        st.markdown(
            f"<h2 style='text-align: center; font-size: 20px;'>Is Open</h2>", unsafe_allow_html=True)
    with c5:
        st.markdown(
            f"<h2 style='text-align: center; font-size: 20px;'>Last Date To Apply</h2>", unsafe_allow_html=True)
    with c6:
        st.markdown(
            f"<h2 style='text-align: center; font-size: 20px;'>Salary</h2>", unsafe_allow_html=True)
    with c7:
        st.markdown(
            f"<h2 style='text-align: center; font-size: 20px;'>Posted By</h2>", unsafe_allow_html=True)
    for i in jobs_all:
        display_job(i)


st.markdown("<hr><h3 style='text-align: center; color: black ;font-size:30px'>VIEW JOBS</h3>",
            unsafe_allow_html=True)

st.text("")
st.text("")

jobs_all = fetch_all_jobs()
if len(jobs_all) != 0:
    display_all_jobs()
else:
    st.markdown("<h3 style='text-align: center; color: red ;font-size:22px'>No Posted Jobs</h3>",
                unsafe_allow_html=True)

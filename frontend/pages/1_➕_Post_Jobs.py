# Libraries
import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Config
st.set_page_config(page_title='Recruitment Data Platform',
                   page_icon=':bar_chart:', layout='wide')

st.markdown("<h1 style='text-align: center; color: #014b94 ;font-size:50px'>RECRUITMENT DATA PLATFORM</h1>",
            unsafe_allow_html=True)

requirements_list = ['Python', 'Java', 'C++', 'AWS',
                     'Docker', 'Power BI', 'Jenkins', 'Kubernetes', 'C#', 'DBMS']


def get_employee_details():
    employees = requests.get(
        'https://employee-data-platform.vercel.app/api/fetchall')
    # print(employees.json())
    return employees.json()


def fetch_all_employee_names(employee_data):
    employee_names = {}
    for employee in employee_data:
        name = employee['first_name']+' '+employee['last_name']
        employee_names[name] = employee['id']
    return employee_names


def employee_divsion_mapping(employee_data):
    employee_department = {}
    for employee in employee_data:
        name = employee['department_name']
        employee_department[name] = employee['department_id']
    return employee_department


def get_requirements(req_list):
    req = ""
    for i in range(0, len(req_list)-1):
        req = req_list[i]+","
    req += req_list[-1]
    return req


def submit(jobtitle, jobdescription, postedby, requirements, salary, lastdate, division):
    requirements = get_requirements(requirements)
    posted_by = employee_names[postedby]
    division = employee_divisions[division]
    lastdate = lastdate.strftime("%Y-%m-%d")
    salary = int(salary)
    headers = {"Content-type": "application/json"}
    data = {"jobTitle": jobtitle, "postedBy": posted_by, "isOpen": True, "jobDescription": job_description,
            "requirements": requirements, "salary": salary, "lastDateToApply": lastdate, "divisionId": division}
    print(data)
    resp = requests.post(
        'https://cc-lab-rdp.azurewebsites.net/jobs/add', json=data, headers=headers)
    print(resp.text)


employee_all = get_employee_details()
employee_names = fetch_all_employee_names(employee_all)
employee_divisions = employee_divsion_mapping(employee_all)
print(employee_divisions)

r1_c1, r1_c2, r1_c3 = st.columns(3, gap="medium")

with r1_c2:
    current_employee = st.selectbox(
        "Current User", list(employee_names.keys()))

st.markdown("<hr><h3 style='text-align: center; color: black ;font-size:30px'>POST JOBS</h3>",
            unsafe_allow_html=True)

st.text("")
st.text("")

r2_c1, r2_c2, r2_c3, r2_c4 = st.columns([5, 4, 4, 5], gap='medium')


with r2_c2:
    jobtitle = st.text_input("Job Title", disabled=False)

with r2_c3:
    posted_by = st.text_input(
        "Posted By", value=current_employee, disabled=False)

r3_c1, r3_c2, r3_c3 = st.columns([4, 7, 4], gap='large')

with r3_c2:
    job_description = st.text_area("Job Description", height=15, max_chars=200,
                                   placeholder="Type a job description here")

r4_c1, r4_c2, r4_c3, r4_c4 = st.columns([5, 4, 4, 5], gap='medium')


with r4_c2:
    requirements = st.multiselect("Requirements", options=requirements_list)

with r4_c3:
    last_date_to_apply = st.date_input("Last Date to Apply")

r5_c1, r5_c2, r5_c3, r5_c4 = st.columns([5, 4, 4, 5], gap='medium')


with r5_c2:
    salary = st.number_input("Salary")

with r5_c3:
    division = st.selectbox("Division", list(employee_divisions.keys()))

st.text("\n\n")

r6_c1, r6_c2, r6_c3 = st.columns([10, 3, 9], gap='medium')

with r6_c2:
    global submit_status
    if st.button('Post Job', type="primary"):
        submit(jobtitle=jobtitle, postedby=posted_by, requirements=requirements,
               lastdate=last_date_to_apply, salary=salary, jobdescription=job_description, division=division)

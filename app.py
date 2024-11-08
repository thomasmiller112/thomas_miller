import requests
import streamlit as st

def analyze_job_description(job_description):
    # Your code here
    body = {
        "job_description": job_description
    }
    
    res = requests.post("https://hook.us1.make.com/u1fejh810y0txuw4wkwwnjx2lpk4ig7v", json=body)
    return res.text

if 'run_button' in st.session_state and st.session_state.run_button == True:
    st.session_state.running = True
else:
    st.session_state.running = False
    

st.write("""
# Job Analyzer
         """)





text = st.text_area("Enter the job description here", height=200)


x,y = st.columns(2)

data = None



if y.button("Analyze Job Description & Download Resume", disabled=st.session_state.running, key='run_button'):
    st.write("Downloading Resume...")
    data = analyze_job_description(text)
    
if data:
    st.write("Resume Created Successfully!")
    st.link_button("View Resume", data)
    
    
    
    

import streamlit as st
from pdfextractor import text_extractor
import google.generativeai as genai
import os

# Configure the model 
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-2.5-flash-latest')


# Upload resume 
st.sidebar.title(':blue[UPLOAD YOUR RESUME ( PDF ONLY)]')
file=st.sidebar.file_uploader('Resume',type=['pdf'])

if file:
    resume_text=text_extractor(file)
    st.write(resume_text)

# Least define the main page

st.title(':orange[SKILLMATCH]: :blue[AI Assisted Skill Matching Tool]')
st.markdown('##### This application will match your resume and the job description.It will create a detailed report on the match')
tips = '''Follow these steps to proceed :
* Upload your resume in the sidebar (PDF only)
* Copy and paste the job description below for which you are applying
* Click the button and see the magic.'''
st.write(tips)

job_desc = st.text_area('Copy and paste Job Discription here',max_chars=10000)

prompt = ''' Assume you are expert in skill matching and creating profiles
Match the following resume with the job description provided by the user
resume = {resume_text}
job desciption = {job_desc}

Your output should be as follows :
* Give a brief description of the applicant in 3-5 lines.
* Give a range of expected ATS score along with the matching and non matching key words
* Give the chances of getting shortlisted for this position in percentage
* Perform SWOT analysis and discuss each and everything in bullet points
* Suggest all imporvements that can be made in the resume in order to get better ATS and increase the percentage of getting shortlisted.
* Also create the customised resumes as per the job description provides to get better ATS and increase the percentage of getting shortlisted
* Prepare a one page resume in such a format that can be copied and pasted in word
* Use bullet points and tables where ever required.'''

button = st.button('click')
if button :
    if resume_text and job_desc:
        response = model.generate_content(prompt)
        st.write(response_text)
    else:
        st.write('Please upload resume and provide job description')
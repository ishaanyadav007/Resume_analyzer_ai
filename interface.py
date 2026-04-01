import streamlit as st
from analysis import analyze_resume

st.set_page_config(page_title='AI Resume analyzer',page_icon='📑',layout='wide',initial_sidebar_state='expanded')
st.title('AI Resume Analyzer 🤖 📃')
st.subheader('This webpage helps you to compare your resume with the relevant job description.')
st.sidebar.subheader('Drop your resume here: ⬇️')
pdf_doc = st.sidebar.file_uploader('Click here to browse:',type=['pdf'])

st.sidebar.markdown('Designed by **Ishaan Yadav**')
st.sidebar.markdown('Github profile: _https://github.com/ishaanyadav007_ ')

job_des = st.text_area('Copy and paste the JD here 👉🏻')
score = st.button('Generate score📊:')

if score:
    with st.spinner('Generating results...'):
        analyze_resume(pdf_doc,job_des)
        




















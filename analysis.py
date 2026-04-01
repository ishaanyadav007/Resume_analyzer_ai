import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv(override=True)

import google.generativeai as genai
from pdf import extractpdf          # we are importing a class/function from another python file pdf.py that we created ourselves

key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-2.5-flash')

def analyze_resume(pdf_doc,job_desp):
    
    if pdf_doc is not None:
        pdf_text = extractpdf(pdf_doc)      # class in pdf.py will run
        st.write('Extracted successfully✅')
    
    else:
        st.warning('Error drop file in pdf format❌.')
    
    ats_score = model.generate_content(f'''Compare the resume {pdf_text} and job description 
                                   {job_desp} and get the ATS score on a scale of 0 to 100.
                                   Generate the results in bullet points.''')
    prob_score = model.generate_content(f'''Compare the resume {pdf_text} and job description 
                                   {job_desp} and give the probability in percent from 0 to 100 as 
                                   to whether the candidate will be selected for the job or not.''')
    good_fit = model.generate_content(f'''Compare the resume {pdf_text} and the job desription
                                      {job_desp} and tell if the candidate is a good fit for the job or not.
                                      If not tell in what areas the candidate lacks and suggest areas of improvement.''' )
    swot_analysis = model.generate_content(f'''Compare the resume {pdf_text} and the job desription
                                      {job_desp} and provide SWOT analysis. Generate minimum 3 points for each analysis.''')
    
    return {st.write(ats_score.text),
            st.write(prob_score.text),
            st.write(good_fit.text),
            st.write(swot_analysis.text)}
            

        

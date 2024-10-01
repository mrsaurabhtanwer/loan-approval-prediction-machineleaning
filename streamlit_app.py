
import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Loan Prediction App')
st.markdown('A simple app to predict loan approval based on user input')

# Add a form to collect user input
st.header('User Input')
col1, col2 = st.columns(2)
with col1:
    st.text('Applicant Information')
    applicant_income = st.number_input('Applicant Income', min_value=0, max_value=1000000, value=50000)
    coapplicant_income = st.number_input('Coapplicant Income', min_value=0, max_value=1000000, value=50000)
with col2:
    st.text('Loan Information')
    loan_amount = st.number_input('Loan Amount', min_value=0, max_value=1000000, value=50000)
    loan_term = st.number_input('Loan Term', min_value=1, max_value=360, value=12)

# Add a button to make predictions
if st.button('Predict'):
    # Call the predict function from your prediction.py file
    result = predict(np.array([[applicant_income, coapplicant_income, loan_amount, loan_term]]))
    st.text(result[0])


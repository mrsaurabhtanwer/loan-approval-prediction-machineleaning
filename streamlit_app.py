import streamlit as st
import pandas as pd
import numpy as np


st.title(' Loan Approval Prediction')

st.info(' Here you can predict your loan eligibility certria')
df =pd.read_csv('https://github.com/mrsaurabhtanwer/Loan-Approval-Prediction-using-Machine-Learning-/blob/main/Copy%20of%20loan%20-%20loan.csv')
df


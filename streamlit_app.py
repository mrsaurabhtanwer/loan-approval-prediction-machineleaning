import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn import svm


st.title(' Loan Approval Prediction')

st.write(' Here you can predict your loan eligibility certria')
 df=pd.read_csv("https://github.com/mrsaurabhtanwer/Loan-Approval-Prediction-using-Machine-Learning-/blob/main/Copy%20of%20loan%20-%20loan.csv")



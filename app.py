## This app generates the configuration 

import streamlit as st 
import pandas as pd
import numpy as np



st.write("""
## Rules Engine for Customer Decisioning 
""")

#Load Data
df = pd.read_csv('dummy_data.csv')


with st.expander('Click for Dummy Data Snapshot'):
    # Add user input widgets to the side bar
    st.write(df.head())


st.write("## Rules Hierarchy")
st.write("#### Account Opened -> Remote Check Deposit -> Account Funded -> Credit Card Issued -> Direct Deposit -> Mobile App Downloaded -> Update Contact Info")
st.text("")
st.text("")

#List of all customer IDs
custID = df.CustID.values
st.sidebar.write("Select Customer ID")
selected_id = st.sidebar.selectbox('',(custID))
selected_customer = df[df.CustID==selected_id]

#st.write("Customer ID Selected :", selected_id)
st.write("Snapshot of selected customer with Current Account Status:", selected_customer)

def next_action(status):
    if status == 'Account Opened':
        return 'Remote Check Deposit'
    elif status == 'Remote Check Deposit':
    	return 'Account Funded'
    elif status == 'Account Funded':
    	return 'Credit Card'
    elif status == 'Credit Card Issued':
    	return 'Direct Deposit'
    elif status == 'Direct Deposit':
    	return 'Mobile App Download'
    elif status == 'Mobile App Downloaded':
    	return 'Update Contact Info'
    else:
    	return 'No Further Action'


next_action = selected_customer['AccountStatus'].apply(lambda x: next_action(x))

st.write("### Next Action :", next_action.values[0])

import streamlit as st
import pandas as pd
from datetime import datetime

st.title("☀️ Solar Generation Tracker")

# Use the sheet ID from your URL
SHEET_ID = "1fVZlHMdCTaHVE2r0y693kIuIWU21xRLg0fzDuLTDn4Q"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.subheader("Add Daily Reading")
with st.form("entry_form"):
    date_val = st.date_input("Date", datetime.now())
    unit_val = st.number_input("Units", min_value=0.0, step=0.1)
    kw_val = st.number_input("KW Reading", min_value=0.0, step=1.0)
    submitted = st.form_submit_button("Submit Data")

if submitted:
    # IMPORTANT: Since writing back to Sheets via URL alone is restricted by Google,
    # the best way is to use the 'st-gsheets-connection' with the Private Key.
    st.info("To save this data, please ensure the Secrets match the Service Account format exactly.")
    
# Display current data
try:
    df = pd.read_csv(SHEET_URL)
    st.divider()
    st.subheader("Current Data in Sheet")
    st.dataframe(df)
except Exception as e:
    st.error("Could not read sheet. Please ensure 'Anyone with link can Edit' is turned on.")

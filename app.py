import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import calendar
from datetime import datetime

st.title("☀️ Solar Generation Tracker")

# Simplified connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Date Selection
month_names = list(calendar.month_name)[1:]
selected_month = st.selectbox("Select Month", month_names)
month_num = month_names.index(selected_month) + 1
dates = [f"{datetime.now().year}-{month_num:02d}-{day:02d}" for day in range(1, calendar.monthrange(datetime.now().year, month_num)[1] + 1)]

with st.form("entry_form"):
    date_val = st.selectbox("Date", dates)
    unit_val = st.number_input("Units", min_value=0.0)
    kw_val = st.number_input("KW Reading", min_value=0.0)
    submitted = st.form_submit_button("Save to Sheet")

if submitted:
    # Fetch existing data
    df = conn.read()
    # Add new row
    new_data = pd.DataFrame([{"Date": str(date_val), "Units": unit_val, "KW_Reading": kw_val}])
    df = pd.concat([df, new_data], ignore_index=True)
    # Write back
    conn.update(data=df)
    st.success("SUCCESS! Check your Google Sheet now.")
    st.balloons()

# Simple Table View
st.divider()
st.subheader("Current Records")
final_df = conn.read()
st.dataframe(final_df)

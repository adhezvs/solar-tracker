import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title("☀️ Solar Tracker")

# Connect using the "gsheets" secret
conn = st.connection("gsheets", type=GSheetsConnection)

with st.form("entry_form"):
    date_val = st.date_input("Select Date")
    unit_val = st.number_input("Units", min_value=0.0)
    kw_val = st.number_input("KW Reading", min_value=0.0)
    submitted = st.form_submit_button("Save to Sheet")

if submitted:
    try:
        # Read current data
        df = conn.read()
        # Add new row
        new_row = pd.DataFrame([{"Date": str(date_val), "Units": unit_val, "KW_Reading": kw_val}])
        df = pd.concat([df, new_row], ignore_index=True)
        # Update sheet
        conn.update(data=df)
        st.success("✅ Saved!")
    except Exception as e:
        st.error(f"Error: {e}")

# Show data
st.divider()
try:
    data = conn.read()
    st.dataframe(data)
except:
    st.info("No data yet.")

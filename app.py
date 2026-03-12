import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import calendar
from datetime import datetime
import plotly.express as px

st.set_page_config(page_title="Solar Tracker", layout="wide")
st.title("☀️ Solar Generation Tracker")

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# 1. Setup Date Selection
month_names = list(calendar.month_name)[1:]
selected_month = st.selectbox("Select Month", month_names)
month_num = month_names.index(selected_month) + 1
year = datetime.now().year
num_days = calendar.monthrange(year, month_num)[1]
dates = [f"{year}-{month_num:02d}-{day:02d}" for day in range(1, num_days + 1)]

# 2. Input Section
st.subheader(f"Add Reading for {selected_month}")
c1, c2, c3 = st.columns(3)
with c1:
    date_to_fill = st.selectbox("Date", dates)
with c2:
    units = st.number_input("Units (18-20)", min_value=0.0)
with c3:
    kw = st.number_input("KW Reading (5609...)", min_value=0.0)

if st.button("Save Data"):
    # Log logic here
    st.success("Entry recorded! (Requires Step 3 setup to save permanently)")

# 3. Summary & Graph
data = conn.read() # This reads from your sheet
if not data.empty:
    st.divider()
    st.subheader("Monthly Analysis")
    fig = px.bar(data, x="Date", y="Units", title="Units Generated")
    st.plotly_chart(fig)

import streamlit as st
from sheets_service import read_records

st.title("🔗 Test Google Sheets Connection")

sheet_name = "user_map"  # atau sheet lain yang sudah kamu buat
data = read_records(sheet_name)

st.write("📄 Data dari Sheet:")
st.dataframe(data)
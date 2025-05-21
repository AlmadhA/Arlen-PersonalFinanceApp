import streamlit as st
from sheets_service import read_records

st.title("🔗 Test Google Sheets Connection")

sheet_name = "user_map"  # Ubah sesuai sheet yang kamu punya
try:
    data = read_records(sheet_name)
    st.success(f"Berhasil membaca data dari sheet: {sheet_name}")
    st.dataframe(data)
except Exception as e:
    st.error("Gagal membaca dari Google Sheets:")
    st.exception(e)
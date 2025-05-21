import streamlit as st
from google.oauth2 import service_account
import gspread
import pandas as pd

def get_gspread_client():
    creds_info = st.secrets["gcp_service_account"]
    creds = service_account.Credentials.from_service_account_info(creds_info)
    return gspread.authorize(creds)

def read_records(sheet_name):
    client = get_gspread_client()
    spreadsheet_id = st.secrets["spreadsheet_id"]  # Ambil langsung dari root secrets
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    records = sheet.get_all_records()
    return pd.DataFrame(records)
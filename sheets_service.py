import streamlit as st
from google.oauth2 import service_account
import gspread
import pandas as pd

def get_gspread_client():
    creds_info = st.secrets["gcp_service_account"]
    creds = service_account.Credentials.from_service_account_info(
        creds_info,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]  # penting!
    )
    return gspread.authorize(creds)

def read_records(sheet_name):
    client = get_gspread_client()
    spreadsheet_id = st.secrets["spreadsheet_id"]  # Ambil dari root secrets
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    records = sheet.get_all_records()
    return pd.DataFrame(records)

def append_record(sheet_name, record: dict):
    client = get_gspread_client()
    spreadsheet_id = st.secrets["spreadsheet_id"]
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    row = list(record.values())
    sheet.append_row(row)
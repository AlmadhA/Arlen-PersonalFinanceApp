import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_CREDENTIALS_PATH, SPREADSHEET_ID

def get_gsheet_client():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_PATH, scope)
    client = gspread.authorize(creds)
    return client

def get_sheet(sheet_name):
    client = get_gsheet_client()
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    return spreadsheet.worksheet(sheet_name)

def read_records(sheet_name):
    sheet = get_sheet(sheet_name)
    return sheet.get_all_records()

def append_row(sheet_name, row):
    sheet = get_sheet(sheet_name)
    sheet.append_row(row)
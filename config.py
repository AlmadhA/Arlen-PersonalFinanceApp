import os
import json

SPREADSHEET_ID = os.getenv("1PAgc4t9RBbPLpnsoWbC1rgcwH6bX6jK8IcGel-b4cG4")

# Simpan kredensial dari secrets ke file sementara
creds = json.loads(os.getenv("GOOGLE_CREDENTIALS"))
with open("temp_credentials.json", "w") as f:
    json.dump(creds, f)

GOOGLE_CREDENTIALS_PATH = "temp_credentials.json"
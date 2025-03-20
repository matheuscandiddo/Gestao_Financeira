import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

filename = ""

scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename=filename,
    scopes=scopes

)

client = gspread.authorize(creds)
print(client)
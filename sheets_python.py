import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Credenciais de conta --> Com partilhar a pasta e o arquivo no drive manualmente, passar o id da pasta

filename = "projeto-dashboards-financas-d361a0e57bf7.json"

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

planilha_completa = client.open(
    tittle = "receitas_csv",
    folder_id = "1IZfB_UVxbCasWUTLP9u6GO1QGFnF7iAi"
)
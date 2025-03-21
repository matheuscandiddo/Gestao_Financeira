import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Credenciais de conta --> Com partilhar a pasta e o arquivo no drive manualmente, passar o id da pasta

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

planilha_completa = client.open(
    title = "df_receitas",
    folder_id = "1IZfB_UVxbCasWUTLP9u6GO1QGFnF7iAi",
)

planilha = planilha_completa.get_worksheet(0)

dados = planilha.get_all_records()
print(pd.DataFrame(dados))

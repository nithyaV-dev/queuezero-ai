import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("QueueZeroDB").sheet1
    return sheet


def get_all_data():
    sheet = connect_sheet()
    return sheet.get_all_records()


def update_tokens(department, new_tokens):
    sheet = connect_sheet()
    data = sheet.get_all_records()

    for i, row in enumerate(data, start=2):
        if row["Department"] == department:
            sheet.update_cell(i, 2, new_tokens)
            return True

    return False
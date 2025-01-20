import json
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# 配置 Google Sheets API 憑證
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
# 從環境變數中加載憑證
credentials_info = json.loads(os.getenv('GOOGLE_CREDENTIALS_JSON'))
credentials = Credentials.from_service_account_info(credentials_info, scopes=SCOPES)
SPREADSHEET_ID = os.getenv('GOOGLE_SHEET_ID')  # 修改為實際試算表的 ID
service = build('sheets', 'v4', credentials=credentials)

# # 配置 Google Sheets API 憑證
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SERVICE_ACCOUNT_FILE = r"C:\Users\User\Downloads\skilled-script-448314-j0-0c05f20ca146.json"

# credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# service = build('sheets', 'v4', credentials=credentials)

# SPREADSHEET_ID = '1TWp1XNDx46NPLRZQA9AVA1yghVxhA_2TZwwb9c0fIMA'

# 讀取數據
def read_data(range_name):
    """從 Google 試算表中讀取數據"""
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
        return result.get('values', [])
    except Exception as e:
        print(f"Error reading data: {e}")
        return []

print(read_data('表單回應 1!A1'))  # 讀取 Sheet1 表的 A1 區域的數據
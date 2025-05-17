import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

def get_google_sheet_service():
    """구글 시트 API 서비스 객체를 반환합니다.
    
    Returns:
        Resource: 구글 시트 API 서비스 객체
    """
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None

    # 토큰 파일이 있으면 로드
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # 유효한 인증정보가 없으면 새로 생성
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        # 토큰 저장
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('sheets', 'v4', credentials=creds)

def read_sheet_range(spreadsheet_id: str, range_name: str) -> list:
    """지정된 범위의 시트 데이터를 읽어옵니다.
    
    Args:
        spreadsheet_id: 스프레드시트 ID
        range_name: 읽어올 범위 (예: 'Sheet1!A1:D10')
        
    Returns:
        list: 읽어온 데이터 리스트
    """
    try:
        service = get_google_sheet_service()
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        
        return result.get('values', [])
        
    except Exception as e:
        print(f"시트 읽기 오류: {str(e)}")
        return []


def get_sheet_data(spreadsheet_id: str, range_name: str = '동춘!A:O') -> dict:
    get_google_sheet_service()
    # 구글 시트에서 데이터 읽어오기

    print("구글 시트에서 데이터를 읽어오는 중...")
    sheet_data = read_sheet_range(spreadsheet_id, range_name)
    print(sheet_data)
    name_dict = {}

    for row in sheet_data:
        name_dict[row[0]] = row[1:15]

    return name_dict
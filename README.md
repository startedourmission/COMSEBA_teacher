이 프로그램은 문서 작업을 자동화하기 위한 Python 기반 도구입니다. 구글 스프레드시트에서 데이터를 가져오고, 웹 출결 및 상담 정보를 자동으로 업로드하는 기능을 제공합니다. 반복적인 문서 작업을 효율적으로 처리할 수 있도록 설계되었습니다.

### 주요 기능
- 구글 스프레드시트 데이터 자동 수집
- 웹 기반 출결 및 상담 내역 자동 업로드


### 구글 스프레드시트 연동
   1. https://console.cloud.google.com/apis/credentials 에서 OAuth 2.0 Client IDs 클라이언트 json 파일을 다운로드 하세요
   
   2. 다운로드받은 json파일의 이름을 credientials.json으로 바꿔주세요.

   3. main.ipynb 내에 구글 스프레드시트 ID와 시트 이름을 입력하세요.
   
     ```python
     SPREADSHEET_ID = "여기에_스프레드시트_ID_입력"
     SHEET_NAME = "시트이름"
     ```
  4. main.ipynb를 실행하면 웹 상담/출결 자동 업로드를 수행합니다. 

### 자동화 과정
   - selenium이 웹 브라우저를 실행하여 로그인 및 데이터 입력을 자동으로 수행합니다.
   - beautifulsoup4로 웹 페이지에서 필요한 정보를 파싱합니다.
   - PyAutoGUI로 마우스 클릭, 키보드 입력 등 반복 작업을 자동화합니다.


### 의존성
- Python >= 3.8
- selenium 
- beautifulsoup4 

# Gspread-Entry-Log-System
Entry Log System with Python &amp; Google Spreadsheet

-----------------------------------------------------------

구글 스프레드시트를 이용하여 간단히 전자 출입명부를 구현해보았습니다.

본 프로그램은 코로나19 시대의 행사 준비를 위해 짜여졌으며, 행사 전날 급하게 만든 관계로 예상치 못하 각종 오류와 버그가 있을 수 있습니다.

기본적인 기능은 다양한 환경(Mac OS, Windows, Ubuntu) 구동됨을 확인하였습니다. (환경에 맞게 약간의 수정이 필요할 수는 있음)

### 기본 세팅

**1. 사용환경 셋업**

  - 구글 사용자 인증 설정이 필요하고, JSON 파일 형태의 API 키를 다운받아야합니다.
  - [여기](https://yurimkoo.github.io/python/2019/07/20/link-with-googlesheets-for-Python.html)에 자세히 설명되어 있습니다.
  <br/>
  
**2. 패키지 설치**
  - oauth2client와 gspread를 설치해줍니다.
  - ```pip3 install --upgrade oauth2client```
  - ```pip3 install gspread```
  <br/>
  
**3. 코드 수정**
  - 코드의 16번째 줄과 23번째 정보를 입력해줍니다.
  - ```json_file_name = '<your file name>.json'```에 다운받은 json파일을 넣어줍니다.
  - ```spreadsheet_url = '<your URL>'```에 구글 스프레드시트 링크를 넣어줍니다.
<br/>

### 작동 설명

- 작성중

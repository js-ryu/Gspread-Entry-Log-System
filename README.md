# Gspread-Entry-Log-System
Entry Log System with Python &amp; Google Spreadsheet

-----------------------------------------------------------

구글 스프레드시트를 이용하여 간단히 전자 출입명부를 구현해보았습니다.

본 프로그램은 코로나19 시대의 행사 준비를 위해 짜여졌으며, 행사 전날 급하게 만든 관계로 예상치 못한 각종 오류와 버그가 있을 수 있습니다.

기본적으로 RFID(학생증, 사원증) 태그를 통해 출입 위치와 시간을 체크하는 기능을 구현하였습니다. 이 정보는 모두 사전에 설정된 구글 스프레드시트에 기록되어, 중앙 관제가 가능합니다.

기본적인 기능은 다양한 환경(Mac OS, Windows, Ubuntu)에서 구동됨을 확인하였습니다. (환경에 맞게 약간의 수정이 필요할 수는 있음)

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

- 각 출입구에 컴퓨터와 RFID 태그 설치

- 초기 사용자 등록 필요(RFID UID, 이름, 학번, 체온 등)
  - 등록은 특정 장소에서만 가능하게 되어있음.
  - 사전등록자의 경우 이름과 학번은 미리 스프레드시트에 입력해놓을 수 있음.

- 장소 출입 시 RFID 태그 만으로, 언제 어디에 드나들었는지 확인가능

1. 프로그램 실행 시, 컴퓨터 설치 위치 설정 (E1 IN, E1 OUT, E7 IN, E7 OUT)

2. RFID 태그

3.
```
if 등록된 사용자:
    스프레드시트에 장소와 시간 기록
  
else : #등록되지 않은 사용자:
    if 등록 가능 장소가 아닐 경우:
        error!
    
    else :
        등록 의사 확인
        if 등록을 원할 경우:
            학번 입력
            
            if 사전등록된 학번일 경우:
                체온 입력 후 등록 완료
                
            else: # 사전 등록되지 않은 사용자일 경우
                이름 입력
                체온 입력
                등록 완료
```

4. 등록시 UID, 이름, 학번, 체온 기록

5. 이후 RFID 태그시 장소와 일시 자동 기록

### 작동 예시

![IMAGE1](https://user-images.githubusercontent.com/50894726/106323775-4f133f80-62bb-11eb-99f5-3a6dfdf82ece.png)

실제 행사에 사용되었던 스프레드시트 이미지



작동 동영상(썸네일 클릭시 이동)


  




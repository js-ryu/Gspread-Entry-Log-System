'''
pip install --upgrade oauth2client
pip install gspread
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

#TODO input your josn file!
json_file_name = '<your file name>.json'


credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

#TODO input your spreadsheet URL!
spreadsheet_url = '<your URL>'

# 스프레드시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택 하기
worksheet = doc.worksheet('list')


def init_check():
    print("")
    print("본 컴퓨터의 위치를 입력해주세요.")
    print("E1 IN : 1, E1 OUT : 2, E7 IN : 3, E7 OUT : 4")
    mycom = input()

    if not (mycom.isdigit()):
        print("잘못 입력하셨습니다.")
        return False

    mycom = int(mycom)
    if not 0 < mycom < 5 :
        print("잘못 입력하셨습니다.")
        return False

    if mycom == 1:
        print("현재 위치는 E1 IN 입니다.")
    elif mycom == 2:
        print("현재 위치는 E1 OUT 입니다.")
    elif mycom == 3:
        print("현재 위치는 E7 IN 입니다.")
    elif mycom == 4:
        print("현재 위치는 E7 OUT 입니다.")

    print("")
    print("초기 세팅 완료!")   
    print("")
        
    return mycom


def check_uid(mycom):
    print("학생증(사원증)을 태그해주세요.")
    uid = input()
    
    uid_col = worksheet.col_values(1)
    print("")
    if uid in uid_col :
        uid_idx = uid_col.index(uid)
        temp_row = worksheet.row_values(uid_idx+1)
        append_idx = len(temp_row)+1
        worksheet.update_cell(uid_idx+1, append_idx, mycom)
        worksheet.update_cell(uid_idx+1, append_idx+1, str(datetime.datetime.now()))
        print("정상 처리되었습니다.")
        print("")

    else :
        if mycom != 1 :
            print("□■□■□■등록되지 않은 사용자입니다□■□■□■")
            print("")


        else:
            print("□■□■□■등록되지 않은 사용자입니다□■□■□■")
            print("등록하시겠습니까? (Y/N)")
            reply = input()

            if reply == 'y' or reply == 'Y' or reply == 'ㅛ':
                print("")
                print("등록 절차를 수행합니다.")
                print("")
                print("학번을 입력해주세요.")
                stud_id = input()
                stud_col = worksheet.col_values(3)

                if stud_id in stud_col:
                    stud_idx = stud_col.index(stud_id)
                    name_idx = 'B' + str(stud_idx+1)
                    name = worksheet.acell(name_idx).value
                    print("")
                    print("사전등록자",name,"입니다.")
                    print("")
                    print("체온을 입력해주세요.")
                    temp = input()
                    print("")
                    print(name, stud_id, temp, "°C 입니다.")
                    temp_row = worksheet.row_values(stud_idx+1)
                    append_idx = len(temp_row)+1
                    worksheet.update_cell(stud_idx+1, 1, uid)
                    worksheet.update_cell(stud_idx+1, append_idx, temp)
                    worksheet.update_cell(stud_idx+1, append_idx+1, mycom)
                    worksheet.update_cell(stud_idx+1, append_idx+2, str(datetime.datetime.now()))
                    print("등록이 완료되었습니다.")
                    print("")

                else :
                    print("")
                    print("이름을 입력해주세요.")
                    name = input()
                    print("")
                    print("체온을 입력해주세요.")
                    temp = input()
                    print("")
                    print(name, stud_id, temp, "°C 입니다.")
                
                    worksheet.append_row([uid, name, stud_id, temp])
                    uid_col = worksheet.col_values(1)
                    uid_idx = uid_col.index(uid)
                
                    temp_row = worksheet.row_values(uid_idx+1)
                    append_idx = len(temp_row)+1
                    worksheet.update_cell(uid_idx+1, append_idx, mycom)
                    worksheet.update_cell(uid_idx+1, append_idx+1, str(datetime.datetime.now()))
                    print("등록이 완료되었습니다.")
                    print("")
    

            elif reply == 'n' or reply == 'N' or reply == 'ㅜ':
                print("")
                print("등록을 취소하셨습니다.")
                print("")


            else : 
                print("")
                print("잘못 입력하셨습니다.")          
                print("")




if __name__ == "__main__":
    init = False
    while not init:
        init = init_check()

    #TF = False
    while True:
        check_uid(init)




import openpyxl
import os

data_folder = 'data'
try:
    chk_list = os.listdir()
    if data_folder not in chk_list:
        os.mkdir(data_folder)
except Exception as e:
    print(e)

excel_file = 'data/s1_기본엑셀생성.xlsx'

# 엑셀 파일 생성
wb = openpyxl.Workbook()

# 현재 활성화된 시트 선택
ws = wb.active

# 시트 이름 변경
# ws.title = '사용자시트'

# 엑셀 저장
wb.save(excel_file)

print('프로그램 종료!')
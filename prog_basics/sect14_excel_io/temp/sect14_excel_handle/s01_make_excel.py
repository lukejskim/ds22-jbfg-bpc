import openpyxl
import os

try:
    chk_list = os.listdir()
    print(chk_list)
    if 'data' not in chk_list:
        os.mkdir('data')
except Exception as err:
    print(err)

excel_file = 'data/JBFG_임직원.xlsx'

# 엑셀파일생성
wb  = openpyxl.Workbook()

# 현재 활성화된 시트 선택
# ws = wb.active
ws = wb.create_sheet('사용자시트')

# 워크시트 삭제
del wb['Sheet']

# 엑셀파일 저장
wb.save(excel_file)

print("프로그램 종료!!!")
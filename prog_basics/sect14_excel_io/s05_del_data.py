import openpyxl

excel_file = 'data/s3_임직원정보.xlsx'

# 엑셀파일 불러오기
wb = openpyxl.load_workbook(excel_file)

# 워크시트 선택
ws = wb['전북은행']

# 데이터 삭제
del ws['A7']

# 엑셀 저장
wb.save(excel_file)

print('프로그램 종료!')


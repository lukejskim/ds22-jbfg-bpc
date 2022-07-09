# 파일이름 바꾸기(osrename)
from os import rename

folder_path = './data/'
target_file = folder_path + 'mydata.txt'
newname = input('[%s]에 대한 새로운 파일 이름을 입력하세요: ' %target_file)

# new_file = folder_path + newname
new_file = newname
rename(target_file, new_file)
print('[%s] -> [%s] 로 파일이름이 변경되었습니다.' %(target_file, new_file))

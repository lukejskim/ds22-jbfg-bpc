# 파일 삭제하기(osremove)
from os import remove

target_file = './data/mydata_copy.txt'
k = input('[%s] 파일을 삭제하겠습니까? ([y]/n)' %target_file)

if k == 'y' or k == '':
    remove(target_file)
    print('[%s] 파일을 삭제했습니다.' %target_file)


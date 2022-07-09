# 파일 크기 구하기(ospathgetsize)
from os.path import getsize

file1 = './data/mydata.txt'
file2 = './images/company_logo.png'

# OK !!
# file2 = '/Users/user/Dropbox/sect_tech/src_anaconda/images/company_logo.txt.png'

# SyntaxError
# file2 = 'C:\Users\user\Dropbox\sect_tech\src_anaconda\images\company_logo.png'

file_size1 = getsize(file1)
file_size2 = getsize(file2)

print('File Name: %s \t File Size: %d Byte' %(file1, file_size1))
print('File Name: %s \t File Size: %d Byte' %(file2, file_size2))
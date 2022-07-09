# 텍스트 파일 복사하기(read, write)
f = open('./data/mydata.txt', 'r')
h = open('./data/mydata_copy.txt', 'w')

data = f.read()
h.write(data)

h.close()
f.close()

with open('./data/mydata_copy.txt', 'r') as fp:
    data = fp.read()

print(data)

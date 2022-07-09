# Image 파일 복사
origin_img = './images/bpc_logo.png'
copied_img = './images/bpc_logo_copy.png'

# 바이너리 파일 복사하기(read, write)
bufsize = 2**10    # 1KB, 1024
f = open(origin_img, 'rb')
h = open(copied_img, 'wb')

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)

h.close()
f.close()


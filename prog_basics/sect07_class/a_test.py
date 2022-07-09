
chk = isinstance(1234, int)
print('chk : {}'.format(chk))

chk = isinstance('1234', str)
print('chk : {}'.format(chk))

chk = isinstance(' 1234 ', int)
print('chk : {}'.format(chk))

chk = '1234'.isdigit()
print('chk : {}'.format(chk))

chk = '12.34'.isdigit()
print('chk : {}'.format(chk))

chk = '12.34'.isdecimal()
print('chk : {}'.format(chk))

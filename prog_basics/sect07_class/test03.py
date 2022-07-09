
# code = '02'
# print(list('012'))
guide_msg = "가위(0)/바위(1)/보(2) : "
code = input(guide_msg).strip()

if code in list('012'):
    print('True : [{}]'.format(code))
else:
    print('False : [{}]'.format(code))

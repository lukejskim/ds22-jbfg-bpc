import json

data = '''
    {
        "name" : "홍길동",
        "age"  : 20,
        "addr" : {
            "city"  : "서울시",
            "dong"  : "월계동"
        }
    }
'''
with open('data/member.json', 'w') as fp:
    fp.write(data)

with open('data/member.json') as data_file:
    member = json.load(data_file)

print(member)
print(type(member))

print('-'*50)
# 출력 : 홍길동은 20살 이고, 서울시 염창동에 살고 있습니다.
text = "{}은 {}살 이고, {} {}에 살고 있습니다.".format(
    member["name"],
    member["age"],
    member["addr"]["city"],
    member["addr"]["dong"],
)
print(text)

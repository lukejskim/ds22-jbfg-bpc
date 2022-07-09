import json
from pprint import pprint

json_data = {
    'firstname' : '길동',
    'lastname'  : '홍',
    'age'       : 20,
    'country'   : '율도국'
}

# json_code = json.JSONEncoder().encode(json_data)
json_code = json.JSONEncoder(ensure_ascii=False).encode(json_data)
print(json_code)
print(type(json_code))
# print(json_code['country'])

json_code = json.JSONDecoder().decode(json_code)
print(json_code)
print(type(json_code))
print(json_code['country'])

print('-'*50)
text = "{}{}은 {}살 이고, {}에 살고 있습니다.".format(
    json_code['lastname'],
    json_code['firstname'],
    json_code['age'],
    json_code['country'],
)

print(text)
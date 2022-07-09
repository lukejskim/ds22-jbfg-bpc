import json
from pprint import pprint

json_data = {
    'firstname' : '길동',
    'lastname'  : '홍',
    'age'       : 20,
    'country'   : '율도국'
}

json_code = json.JSONEncoder().encode(json_data)
print(json_code)
# pprint(json_code)

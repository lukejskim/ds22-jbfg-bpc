import json

with open('data/girlgroup.json', 'w') as fp:
    data = '[ "소녀시대", "앱터스쿨", "에이핑크", "걸스데이", "우주소녀" ]'
    fp.write(data)

with open('data/girlgroup.json') as data_file:
    girlgroup = json.load(data_file)

print(girlgroup)
print(type(girlgroup))

print('-'*50)
# 출력 : 내가 좋아하는 걸그룹은 에이핑크와 우주소녀입니다.
text = "내가 좋아하는 걸그룹은 {}와 {}입니다.".format(
    girlgroup[2], girlgroup[4]
)
print(text)

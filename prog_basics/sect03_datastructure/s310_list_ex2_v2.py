# 리스트형 추가/삭제
blackpink_members = ['지수', '제니']
print('블랙핑크\t:', blackpink_members)

blackpink_members.append('로제')
print('append \t:', blackpink_members)

blackpink_members.insert(1, '리사')
print('insert \t:', blackpink_members)

blackpink_members.remove('제니')
print('remove \t:', blackpink_members)

pickup = blackpink_members.pop(0)
print('pop   \t:', blackpink_members, end=' ---> ')
print(pickup)

test = '파이썬 프로그래밍 재미있다!'    # 문자열을 변수에 저장

result = test.startswith('파이썬')         # 문자열이 '파이썬으로 시작하는지 확인
print(result)
result = test.endswith('!')               # 문자열이 '!'로 끝나는지 확인
print(result)
result = test.endswith('어려워요!')        # 문자열이 '어려워요!'로 끝나는지 확인
print(result)
result = test.replace('파이썬', 'Python')   # 문자열중 '파이썬'을 'Python'으로 변경
print(result)


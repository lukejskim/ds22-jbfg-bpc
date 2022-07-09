import re

# 테스트용 문자열 저장
text = 'My id number is [G203_5A]'
print("# 테스트 문자열 : %s \n%s" % (text, '-'*50))

# 소문자 a 찾기
result = re.findall('a', text)
print(result)

# 대문자 A 찾기
result = re.findall('A', text)
print(result)

# 소문자 i 찾기
result = re.findall('i', text)
print(result)

# 소문자 찾기
result = re.findall('[a-z]', text)
print(result)

# 소문자 연속해서 찾기
result = re.findall('[a-z]+', text)
print(result)

# 대문자 찾기
result = re.findall('[A-Z]', text)
print(result)

# 숫자 찾기
result = re.findall('[0-9]', text)
print(result)

# 숫자 연속해서 찾기
result = re.findall('[0-9]+', text)
print(result)

# 영문자 및 숫자 찾기
result = re.findall('[a-zA-Z0-9]', text)
print(result)

# 영문자 및 숫자 연속해서 찾기
result = re.findall('[a-zA-Z0-9]+', text)
print(result)

# 영문자/숫자 아닌 문자 찾기
result = re.findall('[^a-zA-Z0-9]', text)
print(result)

# 영문자 및 '_'특수기호 찾기
result = re.findall('[\w]', text)
print(result)

# 영문자 및 '_'특수기호 연속해서 찾기
result = re.findall('[\w]+', text)
print(result)

# 영문자 및 '_'특수기호 아닌 문자 찾기
result = re.findall('[\W]', text)
print(result)

import re                   # Regular Expression 모듈 탑재


# 테스트용 문자열 저장
num = int()
text = 'My id number is [G203_5A]'
print("# 테스트 문자열 : %s \n%s" % (text, '-'*50))

# 소문자 a 찾기
result = re.findall('a', text)
num+=1; print("%s) 소문자 a 찾기 : re.findall('a', text) \n \t %s" % (num, result))

# 대문자 A 찾기
result = re.findall('A', text)
num+=1; print("%s) 대문자 A 찾기 : re.findall('A', text) \n \t %s" % (num, result))

# 소문자 i 찾기
result = re.findall('i', text)
num+=1; print("%s) 소문자 i 찾기 : re.findall('i', text) \n \t %s" % (num, result))

# 소문자 찾기
result = re.findall('[a-z]', text)
num+=1; print("%s) 소문자 찾기 : re.findall('[a-z]', text) \n \t %s" % (num, result))

# 소문자 연속해서 찾기
result = re.findall('[a-z]+', text)
num+=1; print("%s) 소문자 연속해서 찾기 : re.findall('[a-z]+', text) \n \t %s" % (num, result))

# 대문자 찾기
result = re.findall('[A-Z]', text)
num+=1; print("%s) 대문자 찾기 : re.findall('[A-Z]', text) \n \t %s" % (num, result))

# 숫자 찾기
result = re.findall('[0-9]', text)
num+=1; print("%s) 숫자 찾기 : re.findall('[0-9]', text) \n \t %s" % (num, result))

# 숫자 연속해서 찾기
result = re.findall('[0-9]+', text)
num+=1; print("%s) 숫자 연속해서 찾기 : re.findall('[0-9]+', text) \n \t %s" % (num, result))

# 영문자 및 숫자 찾기
result = re.findall('[a-zA-Z0-9]', text)
num+=1; print("%s) 영문자 및 숫자 찾기 : re.findall('[a-zA-Z0-9]', text) \n \t %s" % (num, result))

# 영문자 및 숫자 연속해서 찾기
result = re.findall('[a-zA-Z0-9]+', text)
num+=1; print("%s) 영문자 및 숫자 연속해서 찾기 : re.findall('[a-zA-Z0-9]+', text) \n \t %s" % (num, result))

# 영문자/숫자 아닌 문자 찾기
result = re.findall('[^a-zA-Z0-9]', text)
num+=1; print("%s) 영문자/숫자 아닌 문자 찾기 : re.findall('[^a-zA-Z0-9]', text) \n \t %s" % (num, result))

# 영문자 및 '_'특수기호 찾기
result = re.findall('[\w]', text)
num+=1; print("%s) 영문자 및 '_'특수기호 찾기: re.findall('[\w]', text) \n \t %s" % (num, result))

# 영문자 및 '_'특수기호 연속해서 찾기
result = re.findall('[\w]+', text)
num+=1; print("%s) 영문자 및 '_'특수기호 연속해서 찾기: re.findall('[\w]+', text) \n \t %s" % (num, result))

# 영문자 및 '_'특수기호 아닌 문자 찾기
result = re.findall('[\W]', text)
num+=1; print("%s) 영문자 및 '_'특수기호 아닌 문자 찾기 : re.findall('[\W]', text) \n \t %s" % (num, result))

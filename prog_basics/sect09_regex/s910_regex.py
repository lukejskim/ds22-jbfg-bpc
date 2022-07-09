import re                   # Regular Expression 모듈 탑재

# 테스트용 문자열 저장
text = 'My id number is [G203_5A]'
print("# 테스트 문자열 : %s \n%s" % (text, '-'*50))

result = re.findall('[a-z]', text)
print(result)



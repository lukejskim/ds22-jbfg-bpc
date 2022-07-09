name = '홍길동'
greeting = '안녕'

print(name, greeting)
print(greeting, name)

text = name + '님, ' + greeting + '하세요'
print(text)

# "홍길동님 안녕하세요"
print("%s님, %s하세요"%(name, greeting))

print("{}님, {}하세요".format(name, greeting))



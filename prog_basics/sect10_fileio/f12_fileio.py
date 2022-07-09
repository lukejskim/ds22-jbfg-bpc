with open("./data/subject.txt", "w", encoding="UTF-8") as fp:
    data = " 데이터분석과정"
    data+= "\n Python Based Programming"
    fp.write(data)

with open("./data/subject.txt", "r", encoding="UTF-8") as fp:
    data = fp.read()

print(data)

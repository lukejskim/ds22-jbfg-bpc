with open("./data/subject.txt", "w") as fp:
    data = "파이썬 프로그래밍"
    fp.write(data)

with open("./data/subject.txt", "r") as fp:
    data = fp.read()

print(data)

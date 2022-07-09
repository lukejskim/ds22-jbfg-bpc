
def read_csv(filename):
    # 파일데이터 읽어오기
    fp = open(filename, "r", encoding="utf-8")
    data = fp.read()
    fp.close()

    elements = []      # 최종 리턴하기 위한 리스트 변수

    rows = data.split("\n")     # 데이터를 한줄씩 구분하여 리스트로 담기
                                # keys 고정

    keys = rows[0].split(",")
    keys = [key.replace(" ", "") for key in keys]
    print("keys2 : {}".format(keys))
    # print("[{}]".format(keys[1]).replace(" ", ""))

    for row in rows[1:]:
        fields = row.split(",")      # 한줄 데이터를 콤마(,)로 구분하여 리스트로 담기
        # print(fields)

        element = dict()
        for idx in range(len(keys)):
            key = keys[idx]
            field = fields[idx].strip()
            # print(key, field)
            element[key] = field
        # print(element)

        elements.append(element)     # 한줄 데이터를 dict()형으로 변환후 리스트에 추가

    return elements

# filename = "./data/students.csv"      # CSV파일명
filename = "./data/company.csv"      # CSV파일명
students = read_csv(filename)         #

# print(students)

for student in students:
    print(student)

# print('-'*50)
# print(students[0]['이름'])
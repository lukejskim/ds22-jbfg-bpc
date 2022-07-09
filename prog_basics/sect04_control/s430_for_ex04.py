# 삼각형1
for i in range(1, 10, 2):
    mark = "*" * i
    print(mark)








print('\n\n\n')
# 삼각형2
for i in range(1, 10, 2):
    # mark = " " * int((10-i)/2) + "*" * i
    mark = " {space}{star} ".format(
                space = " " * int((10-i)/2),
                star  = "*" * i)
    print(mark)


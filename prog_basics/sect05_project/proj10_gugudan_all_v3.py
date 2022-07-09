# 구구단 전체 출력
cols = 5
rows = int(8/cols)+1
w_space = '\t\t'*2

for row in range(rows):

    dans = list()
    for col in range(cols):
        dan = (row * cols) + col + 2
        dans.append(dan)

    for num in range(10):
        for dan in dans:
            if dan > 9:
                continue

            if num<1:
                print('{}단  \t'.format(dan), end=w_space)
            else:
                gugutext = '{} x {} = {}'.format(dan, num, dan*num)
                print(gugutext, end=w_space)
        print()

    print()


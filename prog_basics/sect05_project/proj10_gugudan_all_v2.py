# 구구단 전체 출력
cols = 4
rows = int(8/cols) + 1

for row in range(rows):

    for col in range(cols):
        dan = (row * cols) + col + 2
        w_space = '\t\t'

        for num in range(10):
            if num<1:
                print('{}단'.format(dan), end=w_space)
            else:
                gugutext = '{} x {} = {}'.format(dan, num, dan*num)
                print(gugutext, end=w_space)
        print()

    print()

# for m in range(2, 10):
#     print('%s \n\t[%d 단 출 력]' % ('='*20, m))
#     for n in range(1, 10):
#         print('\t {} x {} = {}'.format(m, n, m*n))


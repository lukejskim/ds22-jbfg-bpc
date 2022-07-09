#pass 문 예시

signals = 'Red', 'Green', 'Blue'

for x in range(len(signals)):
    print(x, signals[x], '루프 시작!')
    if signals[x] == 'Green':
        pass
    print(x, signals[x], '루프 종료!!')

print('프로그램 종료!!!')

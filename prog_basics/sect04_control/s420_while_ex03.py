# numbers = list(range(10))
numbers = [10, 11, 12, 13, 4, 5, 6, 7, 8, 9]

# numbers[-1]
print('numbers :', numbers)
idx, sum = 0, 0

while idx < len(numbers):
    num = numbers[idx]
    sum += num
    idx += 1

print('numbers의 합계는 %d 입니다.' % sum)


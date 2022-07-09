def add(num1, num2):
    result = num1 + num2
    return result

def add2(num1, num2, num3=0, num4=0):
    result = num1 + num2 + num3 + num4
    return result

def add3(nums):
    result = 0
    for num in nums:
        result += num
    return  result

def add4(*nums):
    result = 0
    for num in nums:
        result += num
    return  result


# sum  =  add(1, 2)
# sum  =  add2(1, 2, 3, 4)
# sum = add3([1, 2, 34, 45, 34])
sum = add4(1, 2, 34, 45, 34, 33)
print(sum)
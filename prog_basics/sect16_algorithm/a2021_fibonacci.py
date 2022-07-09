def fibonacci(num):
    ret_num = int()
    num = int(num)

    if num == 0:
        ret_num = 0
    elif num == 1:
        ret_num = 1
    else:
        ret_num = fibonacci(num - 1) + fibonacci(num - 2)

    return ret_num


for num in range(25):
    print("Fibonacci({}) = {}".format(num, fibonacci(num)))


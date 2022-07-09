def cs_num(num):
    ret_num = str()

    str_num = str(num)
    # rev_num = list(str_num[::-1])
    rev_num = str_num[::-1]
    tmp_num = ''

    print(type(rev_num), rev_num)

    for i in range(len(rev_num)):
        if i>0 and  i%3 == 0:
            tmp_num += ','
        tmp_num += rev_num[i]
        # print(i, tmp_num)

    ret_num = tmp_num[::-1]
    return ret_num

num = 1234567890

# str_num = str(num)
# print(str_num[::-1])

print(cs_num(num))
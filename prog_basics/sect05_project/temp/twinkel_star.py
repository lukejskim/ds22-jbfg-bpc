import turtle as t

# for x in range(1,19):
#     t.forward(100)
#     if x % 2 ==  0:
#         t.left(175)
#     else:
#         t.left(225)
#
# t.done()


def mystar(size, is_filled):
    if is_filled == True:
        t.begin_fill()

    for x in range(1,19):
        t.forward(size)
        if x % 2 ==  0:
            t.left(200-25)
        else:
            t.left(200+25)

    if is_filled == True:
        t.end_fill()

    t.done()

t.color(0.9, 0.7, 0.0)
size = 200
is_filled = True
mystar(size, is_filled)

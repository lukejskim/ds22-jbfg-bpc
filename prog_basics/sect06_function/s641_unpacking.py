

def get_area(w, h):
    return w*h

data = 10, 20    # tuple
# print(type(data))
# print(get_area(data))
print(get_area(*data))  # unpacking




def introduce(name, greeting):
    return "{name}님, {greeting}".format(
        name=name,
        greeting=greeting,
    )

introduce_dict = {
    "name" : "김진수",
    "greeting" : "안녕하세요",
}
print(introduce(**introduce_dict))

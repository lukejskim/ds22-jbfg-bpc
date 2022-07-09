def trace_deco(func):
    def decorator():
        print("begin function!")
        func()
        print("after function!")

    return decorator

@trace_deco
def something():
    print("something!!")

something()
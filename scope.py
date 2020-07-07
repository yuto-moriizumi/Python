var = 1


def add_ten(x):
    global var
    var = 10
    print(var + x)


add_ten(2)    # 12
print(var)     # 10

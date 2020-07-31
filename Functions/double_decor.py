def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner


def num():
    return 4


result_decor = decor(num)
print(result_decor())

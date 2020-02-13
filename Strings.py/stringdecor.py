def decorfun(fun):
    def inner(n):
        result= fun(n)
        return result + " How are you ?"
    return inner 


@decorfun
def hello(name):
    return "Hello "+ name


print(hello("Kumar"))
import functools


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, *kwargs)
        print("End")
    return wrapper


@my_decorator
def hello():
    print("Hello")


# hello = my_decorator(hello)
# hello()

@my_decorator
def say_hello(name):
    print(f"Hello {name}!")


# say_hello("Kumar")


def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start.....")
        result = func(*args, **kwargs)
        print("End......")
        return result
    return wrapper


@my_decorator
def add5(x: int) -> int:
    return x + 5


print(add5(20))
print(add5.__name__)


# A general decorator
def decorator_name(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # some code
        result = func(*args, **kwargs)
        # some code
        return result
    return wrapper


# Decorator with args
def decorator_args(repeat):
    def inner(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(repeat):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return inner


@decorator_args(repeat=10)
def say_hello(name):
    print(f"Hello {name}!")


say_hello("KS")

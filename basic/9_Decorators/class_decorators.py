# class as a decorator


class MyDecorator:
    def __init__(self, func) -> None:
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwags):
        print("START")
        print(f"This is the {self.call_count} call of {self.func.__name__}")
        result = self.func(*args, **kwags)
        print("END")
        self.call_count += 1
        return result


@MyDecorator
def func(name):
    print(f"Welcome {name}!")


func("Kumar Shanu")
func("Alex")

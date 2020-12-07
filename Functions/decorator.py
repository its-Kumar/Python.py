import time


# decorator
def time_it(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(fun.__name__ + " took " + str((end - start) * 1000) + " mil second ")
        return result

    return wrapper


# @time_it
def square(numbers):
    result = []
    for i in numbers:
        result.append(i * i)
    return result


@time_it
def cube(numbers):
    result = []
    for i in numbers:
        result.append(i * i * i)
    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(square(arr))
    print(cube(arr))

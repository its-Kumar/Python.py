# Kumar Shanu
# Make your own range() function in python

# My range() function
class my_range:
    _start = 0
    _stop = 1
    _step = 1
    _count = 0
    _len = 0

    def __init__(self, *args):
        start, stop, step = 0, 10, 1

        if len(args) == 1:
            start, stop, step = 0, args[0], 1

        elif len(args) == 2:
            start, stop, step = args[0], args[1], 1

        elif len(args) == 3:
            start, stop, step = args[0], args[1], args[2]

        else:
            raise TypeError("my_range() takes 1-3 arguments")

        try:
            start, stop, step = int(start), int(stop), int(step)

        except ValueError:
            raise TypeError("an integer is required")

        if step == 0:
            raise ValueError("my_range() arg 3 not be zero")
        elif step < 0:
            stop = min(start, stop)
        else:
            stop = max(start, stop)

        self._start = start
        self._stop = stop
        self._step = step
        self._len = abs(stop - start)
        self._val = start - step

    def __len__(self):
        return self._len

    def __iter__(self):
        return self

    def __next__(self):
        self._val += self._step
        self._count += 1
        if self._count > self._len:
            raise StopIteration()
        return self._val


if __name__ == "__main__":

    # Default range() function
    print("From built-in range()")
    print(type(range))

    # ascending
    for i in range(1, 10, 1):
        print(i)

    print()
    # descending
    for i in range(10, 1, -1):
        print(i)

    input()

    print("From my_range()")

    # ascending
    for i in my_range(0, 10):
        print(i)

    print()
    # descending
    for i in my_range(11, 0, -1):
        print(i)

    # m = my_range(1, 5)
    # print(next(m))
    # print(next(m))
    # print(next(m))
    # print(next(m))

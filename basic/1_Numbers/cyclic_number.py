def sumofdig(num: int):
    s: int = 0
    n: int = 0
    while num:
        s += num % 10
        n += 1
        num //= 10
    return s, n


def is_cyclic(num: int) -> bool:
    s, n = sumofdig(num)
    for i in range(1, n + 1):
        newsum, _ = sumofdig(num * i)
        if newsum != s:
            return False
    return True


for i in range(100, 1000):
    if is_cyclic(i):
        print(i)
    # print(f"{i=}, {isCyclic(i)=}")

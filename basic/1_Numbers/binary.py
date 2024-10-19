lst = []


def binary(num: int):
    if num == 0:
        return lst
    d = num % 2
    lst.append(d)
    binary(num // 2)


if __name__ == "__main__":
    n = int(input("Enter a number : "))
    binary(n)
    lst.reverse()
    for i in lst:
        print(i, end="")

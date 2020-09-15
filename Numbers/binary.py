list = []


def binary(num):
    if num == 0:
        return list
    d = num % 2
    list.append(d)
    binary(num // 2)


if __name__ == "__main__":
    n = int(input("Enter a number : "))
    binary(n)
    list.reverse()
    for i in list:
        print(i, end="")

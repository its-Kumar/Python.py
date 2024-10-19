"""
    A strange root is a number whose squar and squar root share any digit.
    INPUT : 11
    OUTPUT : True
"""


def is_strange_root(n: int) -> bool:
    sqrt = n ** 0.5
    sqrt = str(sqrt).split(".")[1]
    sqr = n ** 2
    sqr = str(sqr).split(".")[0]
    print(sqr, sqrt)
    for d in sqr:
        if d in sqrt:
            return True
    return False


if __name__ == "__main__":
    num = int(input("Enter any number : "))
    print(is_strange_root(num))

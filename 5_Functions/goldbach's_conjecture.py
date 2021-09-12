import random
import sys


def isprime(num):
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def goldbach(num):
    a, b = 0, 0
    while True:
        a = random.randint(1, num)
        b = random.randint(1, num)
        if isprime(a) and isprime(b):
            if (a + b) == num:
                return a, b


if __name__ == "__main__":
    num = int(input("Enter any even number : "))
    if num % 2 != 0:
        print("No is not even..!!")
        sys.exit()
    result = goldbach(num)
    print(result)

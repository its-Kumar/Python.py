def sum_of_dig(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_dig(num//10)


if __name__ == "__main__":
    n = int(input("Enter a number : "))
    print(sum_of_dig(n))

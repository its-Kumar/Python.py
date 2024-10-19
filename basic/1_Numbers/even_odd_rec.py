def is_even(num: int):
    if num < 2:
        return n % 2 == 0
    return is_even(num - 2)


if __name__ == "__main__":
    n = int(input("Enter a number : "))
    if n == 0:
        print("no is zero")
    elif is_even(n):
        print("no is Even.")
    else:
        print("no is Odd.")

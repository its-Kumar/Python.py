def is_ugly(num: int):
    if num == 1:
        return True

    if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0):
        return True
    return False


n = int(input("Enter a number : "))
if is_ugly(n):
    print(n, " is a Ugly number.")
else:
    print(n, " is not a Ugly number.")

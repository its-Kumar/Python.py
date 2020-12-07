def is_prime(num):

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def is_lab_number(num):
    for i in range(2, num):
        if num % i == 0:
            if is_prime(i) and num % i ** 2 == 0:
                return True

    return False


n = int(input("Enter a number : "))
if is_lab_number(n):
    print(f"{n} is a lab number.")
else:
    print(f"{n} is not a lab number.")

r = int(input("Enter a range : "))
for num in range(r):
    if is_lab_number(num):
        print(num)

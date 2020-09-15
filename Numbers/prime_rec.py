def is_prime(num, div=None):
    if div is None:
        div = num - 1
    while div >= 2:
        if (num % div == 0):
            print("Number is not prime...")
            return False
        else:
            return is_prime(num, div - 1)
    else:
        print("Number is prime....")
        return True


if __name__ == "__main__":
    n = int(input("Enter a number : "))
    is_prime(n)

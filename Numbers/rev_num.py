n = input("Enter any number: ")
len_ = len(n)
n = int(n)
result = 0

while n > 0:
    rem = n % 10
    len_ -= 1
    result += rem * 10 ** len_
    n //= 10

print("Reverse = ", result)

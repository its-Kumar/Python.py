n = input("Enter any number: ")
l = len(n)
n = int(n)
result = 0

while n > 0:
    rem = n % 10
    l -= 1
    result += rem * 10 ** l
    n //= 10

print("Reverse = ", result)

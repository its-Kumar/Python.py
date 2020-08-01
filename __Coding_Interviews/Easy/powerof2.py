"""
check if a number is power of 2 or not.
"""

n = int(input('Enter a number : '))

if (n and (n & (n-1)) == 0):
    print(n, "is power of 2.")
else:
    print(n, "not a power of 2.")

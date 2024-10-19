number = int(input("Enter a number : "))
original_number = number

r = 0
while original_number > 0:
    remainder = original_number % 10
    r = r + (remainder ** 3)
    original_number //= 10

if r == number:
    print("Number {:d} is Armstrong".format(number))
else:
    print("Number {:d} is not Armstrong".format(number))

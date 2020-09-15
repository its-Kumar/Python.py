from functools import reduce


def digit_to_num(digits):
    num = reduce(lambda x, y: x * 10 + y, digits)
    return num


dig = [int(x) for x in input("Enter the digits : ").split()]
print("Number is  : ", digit_to_num(dig))

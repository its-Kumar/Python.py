a = int(input("Input a: "))
b = int(input("Input b: "))

print("a = {} , b = {} ".format(a, b))
a, b = b, a
print("a = {} , b = {} ".format(a, b))

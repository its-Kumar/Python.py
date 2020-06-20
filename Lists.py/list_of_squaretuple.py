tmp = [int(x) for x in input("Enter numbers : ").split()]

list = []
for item in tmp:
    tuple = (item, item**2)
    list.append(tuple)


print(list)

tmp = [int(x) for x in input("Enter numbers : ").split()]

list = []
for item in tmp:
    tuple = (item, item**2)
    list.append(tuple)


print(list)


def last(n):
    return n[-1]


list = sorted(list, key=last)
print("Sorted = ", list)

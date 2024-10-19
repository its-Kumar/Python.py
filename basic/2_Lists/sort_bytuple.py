tmp = [int(x) for x in input("Enter numbers : ").split()]

list_ = []
for item in tmp:
    tuple_ = (item, item ** 2)
    list_.append(tuple_)

print(list_)


def last(n):
    return n[-1]


list_ = sorted(list_, key=last)
print("Sorted = ", list)

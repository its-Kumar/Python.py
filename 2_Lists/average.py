lst = [int(x) for x in input("Enter the elements to the list : ").split()]
print(lst)

sum_ = 0
for el in lst:
    sum_ += el

avg = sum_ / len(lst)

print("Average = ", avg)

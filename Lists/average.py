lst = [int(x) for x in input("Enter the elements to the list : ").split()]
print(lst)

sum = 0
for el in lst:
    sum += el

avg = sum / len(lst)

print("Average = ", avg)

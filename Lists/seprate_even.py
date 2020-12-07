lst = [int(x) for x in input("Enter elements to the list : ").split()]

even = []
odd = []

for el in lst:
    if el % 2 == 0:
        even.append(el)
    else:
        odd.append(el)

print("Odd list is {0} , Even list is  {1} ".format(odd, even))

lst = [int(x) for x in input("Enter elements to the list : ").split()]

even, odd = 0, 0
for el in lst:
    if el % 2 == 0:
        if el > even:
            even = el
        else:
            pass
    else:
        if el > odd:
            odd = el
        else:
            pass

print("Max even = {} , Max odd = {} ".format(even, odd))

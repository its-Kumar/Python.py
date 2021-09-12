lst = [int(x) for x in input("Enter elements : ").split()]

even = list(filter(lambda x: x % 2 == 0, lst))
odd = list(filter(lambda x: x % 2 != 0, lst))
print("Even = {} , Odd = {}.".format(even, odd))

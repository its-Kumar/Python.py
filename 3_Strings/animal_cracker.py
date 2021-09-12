def animal_cracker(string):
    lst = string.lower().split()
    return lst[0][0] == lst[1][0]


print(animal_cracker("Hello hii"), animal_cracker("python easy"))

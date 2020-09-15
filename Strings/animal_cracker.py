def Animal_cracker(string):
    lst = string.lower().split()
    return lst[0][0] == lst[1][0]


print(Animal_cracker("Hello hii"), Animal_cracker("python easy"))

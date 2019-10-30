lst1 =[int(x) for x in input("Enter elements to the list : ").split()]
lst2 =[int(x) for x in input("Enter elements to the list : ").split()]

lst=[]
lst.extend(lst1)
lst.extend(lst2)
lst.sort()
print("Merged list : ",lst)

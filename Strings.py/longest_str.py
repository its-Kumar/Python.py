str1 = input("Enter any string : ")
str2 = input("Enter another string : ")

l1=len(str1);  l2=len(str2)

max = max(l1,l2)
if max==l1:
    print("Longest string is : '{}' with lenght {} ".format(str1, l1))
else :
    print("Longest string is : '{}' with lenght {} ".format(str2, l2))
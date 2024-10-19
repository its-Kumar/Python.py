str1 = input("Enter any string : ")
str2 = input("Enter another string : ")

l1 = len(str1)
l2 = len(str2)

max_ = max(l1, l2)
if max_ == l1:
    print("Longest string is : '{}' with length {} ".format(str1, l1))
else:
    print("Longest string is : '{}' with length {} ".format(str2, l2))

str1 = input("Enter a string : ")
str2 = input("Enter another string : ")

s1 = set(str1)
s2 = set(str2)
common = s1 & s2

print("common letters in strings are : ")
for ltr in common:
    print(ltr, end=" ")

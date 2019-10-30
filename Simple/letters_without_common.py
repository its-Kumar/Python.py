str1= input("Enter a string : ")
str2 = input("Enter another string : ")

s1=set(str1);  s2=set(str2)
result = (s1 -s2) | (s2 - s1)

print("Letters of two strings which are not present in both.")
for l in result:print(l,end=" ")


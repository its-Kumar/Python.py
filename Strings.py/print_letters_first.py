str1= input("Enter a string : ")
str2 = input("Enter another string : ")

s1=set(str1);  s2=set(str2)
result = s1-s2

print("Letters of first string which are not in second string : ")
for l in result:print(l,end=" ")

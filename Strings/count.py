str = input("Enter any string : ")
l = len(str)
char = 0
word = 0
for i in range(l):
    char += 1
    if (str[i] == ' '):
        word += 1
        char -= 1

if i != 0:
    word += 1

print("No of characters are : {0} , No of words are : {1}".format(char, word))

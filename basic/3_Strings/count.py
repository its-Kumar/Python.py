s = input("Enter any string : ")
len_ = len(s)
char = 0
word = 0
for i in range(len_):
    char += 1
    if s[i] == " ":
        word += 1
        char -= 1

if i != 0:
    word += 1

print("No of characters are : {0} , No of words are : {1}".format(char, word))

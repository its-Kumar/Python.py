letters = 0
words = 1
try:
    f = open("myfile.txt", "r")
    cont = f.read()
    for c in cont:
        if c == " ":
            words += 1
        else:
            letters += 1

except FileNotFoundError:
    print("File doesnot exists....")

finally:
    f.close()

print("There are {} words and {} letters in the file .".format(words, letters))

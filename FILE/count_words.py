try:
    f = open("myfile.txt", "r")
    cont = f.read()
    l = 0
    w = 1
    for c in cont:
        if c == " ":
            w += 1
        else:
            l += 1

except FileNotFoundError:
    print("File doesnot exists....")

finally:
    f.close()
print("There are {} words and {} letters in the file .".format(w, l))

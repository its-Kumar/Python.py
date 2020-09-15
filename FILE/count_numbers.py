numbers = "0123456789"
try:
    f = open("myfile.txt", "r")
    cont = f.read()
    c = 0
    for d in cont:
        if d in numbers:
            c += 1
            print(d)
        else:
            pass

    print("There are ", c, " numbers in the file.")

except FileNotFoundError:
    print("File doesnot exists....")

finally:
    f.close()

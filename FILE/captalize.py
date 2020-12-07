try:
    with open("myfile.txt", "r") as f:
        line = f.read()
        f.close()
        f = open("myfile.txt", "w")
        line = line.title()
        f.write(line)

except:
    print("File not found ... ")

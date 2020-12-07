try:
    s = open("myfile.txt", "r")
    t = open("copy.txt", "w")
    cont = s.read()
    t.write(cont)

    print("File copied successfully...!!!")

except:
    print("File doesnot present in directory...")

finally:
    t.close()
    s.close()

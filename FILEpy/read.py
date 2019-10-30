try:
    f = open("myfile1.txt","r")
    content = f.read()
    print(content)
    f.close()

except FileNotFoundError:
    print("File doesnot exists...")
    

#finally:
    #f.close()
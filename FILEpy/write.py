try:
    f =open("data.txt","w")
    line = input("Enter a line to the file. ")
    f.write(line)
    
except:
    print("File not found...")
    
finally:
    f.close()
    
print("Write to file successfull...")
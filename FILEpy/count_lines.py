try:
    f =open("myfile.txt","r")
    cont = f.read()
    nl=1
    for c in cont:
        if c =="\n":
            nl +=1
        else:
            pass
        
    
    
except FileNotFoundError:
    print("File doesnot exists....")
    
finally:
    f.close()
    
print("There are ",nl," new lines in the file.")


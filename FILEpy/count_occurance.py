try:
    f =open("myfile.txt","r")
    cont = f.read()
    word = input("Enter the word to be found : ")
    count = cont.count(word)
    print("the word '{}' occurs {} times . ".format(word,count))
    
    
    
except FileNotFoundError:
    print("File doesnot exists....")
    
finally:
    f.close()
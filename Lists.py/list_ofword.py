lst=[x for x in input("Enter words : ").split()]

max =0
w=""
for word in lst:
    if(len(word) > max ):
        max =len(word)
        w = word


print("Word of max length is {} with lenght {}".format(w,max))

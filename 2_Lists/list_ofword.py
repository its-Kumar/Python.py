lst = [x for x in input("Enter words : ").split()]

max_ = 0
w = ""
for word in lst:
    if len(word) > max_:
        max_ = len(word)
        w = word

print("Word of max length is {} with length {}".format(w, max_))

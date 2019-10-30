def paper_doll(string):
    tmp =[]
    for letter in string:
        tmp.append(letter*3)
    return "".join(tmp)


print(
    paper_doll("Hello World.")
)
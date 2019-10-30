def master_yoda(string):
    lst = string.split()
    lst = lst[::-1]
    return " ".join(lst)

print(
    master_yoda("I am home"),
    master_yoda("We are ready.")
)
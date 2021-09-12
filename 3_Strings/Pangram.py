def is_pangram(string: str):
    lst = []
    for i in range(26):
        lst.append(False)

    for char in string:
        if char != " ":
            lst[ord(char) - ord("a")] = True
    return all(lst)


if __name__ == "__main__":
    s = input("Enter any string : ")

    if is_pangram(s):
        print("String is Pangram.")
    else:
        print("String is Not Pangram.")

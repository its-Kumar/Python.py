def count(str,char):
    if not str:
        return 0
    elif str[0]==char:
        return 1 + count(str[1:],char)
    else:
        return count(str[1:],char)


if __name__ == "__main__":
    str = input("Enter string : ")
    char = input("Enter a character : ")
    print(count(str,char))
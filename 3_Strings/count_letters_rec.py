def count(s: str, char):
    if not s:
        return 0
    elif s[0] == char:
        return 1 + count(s[1:], char)
    else:
        return count(s[1:], char)


if __name__ == "__main__":
    s = input("Enter string : ")
    char = input("Enter a character : ")
    print(count(s, char))

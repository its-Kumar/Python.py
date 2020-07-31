
def is_pangram(str):
    list = []

    for i in range(26):
        list.append(False)

    for char in str:
        if char != ' ':
            list[ord(char) - ord('a')] = True

    for c in list:
        if c == False:
            return False

    return True


if __name__ == "__main__":
    s = input("Enter any string : ")

    if is_pangram(s):
        print("String is Pangram.")
    else:
        print("String is Not Pangram.")

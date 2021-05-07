def is_lower(char):
    lower = "abcdefghijklmnopqrstuvwxyz"
    for c in lower:
        if char == c:
            return 1
        else:
            pass
    return 0


def is_upper(char):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in upper:
        if char == c:
            return 1
        else:
            pass
    return 0


if __name__ == "__main__":
    s = input("Enter any string  : ")
    lower = 0
    u = 0
    o = 0
    for char in s:

        if is_lower(char):
            lower += 1
        elif is_upper(char):
            u += 1
        else:
            o += 1

    print("The string contains {} lower , {} upper and {} other characters. "
          .format(lower, u, o))

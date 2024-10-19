def is_prime_string(string: str) -> bool:
    mid = len(string) // 2
    return not (string[:mid] == string[mid:])


if __name__ == "__main__":
    s = input("Enter a string : ")
    if is_prime_string(s):
        print("Prime string")
    else:
        print("Not Prime")

import itertools as it


def is_palindrome(word: str) -> bool:
    """
    Return True if word is a Palindrome
    """
    if word == word[::-1]:
        return True
    return False


def is_anadrome(word: str) -> bool:
    """
    Return True if any Anagram of the given word is a Palindrome.
    """
    anagrams = []
    tmp = list(it.permutations(word))
    for each in tmp:
        anagrams.append("".join(each))

    for w in anagrams:
        if is_palindrome(w):
            print(w)
            return True
    return False


if __name__ == "__main__":
    word = input("Enter any word to check: ")
    if is_anadrome(word):
        print("Yes..!!")
    else:
        print("No..!!")

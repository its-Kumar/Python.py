'''
    PIG LATIN
    1. If word starts with a vowel , add 'ay' to end.
    2. If word does not starts with a vowel, put first letter at the end, then add 'ay'

    word  --> ordway
    apple --> appleay
'''


def pig_latin(w):
    vowels = "aeiouAEIOU"
    lst = list(w)
    if lst[0] in vowels:
        lst.append('ay')
    else:
        p = lst.pop(0)
        lst.extend([p, 'ay'])
    w = ''.join(lst)
    return w


print("\tWelcome to PIG LATIN\n")
word = input("Enter any word : ")
word = pig_latin(word)
print("PIG LATIN Word is  : ", word)

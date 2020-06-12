def Anagram(s1, s2):
    if(len(s1) != len(s2)):
        return 0

    s1 = sorted(s1)
    s2 = sorted(s2)
    if(s1 == s2):
        return 1
    else:
        return 0


str1, str2 = (s for s in input("Enter two strings : ").split())
if(Anagram(str1, str2)):
    print("'{}' and '{}' are Anagrams ".format(str1, str2))
else:
    print("'{}' and '{}' are not Anagrams ".format(str1, str2))

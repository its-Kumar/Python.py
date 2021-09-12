"""Given a function which accept 3 argument. If occurrences of the
second argument in first argument is equal to the third argument
return True else False.

function max_occurrences(str1: str, str2: str, num: int) -> bool:
"""


def max_occurrences(str1: str, str2: str, num: int) -> bool:
    count: int = 0
    i: int = 0
    j: int = 0
    flag: int = 0

    while i < len(str1):
        flag = 0
        j = 0

        if str1[i] == str2[j]:
            while j < len(str2):
                if str1[i] != str2[j]:
                    flag = 1
                    break
                i += 1
                j += 1

            if not flag:
                count += 1
        else:
            i += 1

    return count == num


print(
    max_occurrences("catziraffecattiger", "cat", 2),
    max_occurrences("catziraffecattiger", "cat", 3),
    max_occurrences("ziraffecattiger", "cat", 1),
    max_occurrences("catzifcattiger", "catt", 1),
    max_occurrences("catziraffecattiger", "at", 2)
)

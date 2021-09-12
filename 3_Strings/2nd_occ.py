"""Find the 2nd highest occurring character. If there are multiple of them
then return the first occurring one.
Sample input/output:
secondHighest(“iloveindiamydear”) → e
"""

from collections import defaultdict


def second_highest(s: str):
    d = defaultdict(int)
    for char in s:
        d[char] += 1

    max_1 = -9999
    max_2 = max_1
    for k, v in d.items():
        if v > max_1:
            max_2 = max_1
            max_1 = v
        if v > max_2 and v != max_1:
            max_2 = v
        # print(k, v, max_1, max_2)
    print(d)

    for k in d:
        if d[k] == max_2:
            return k


print(second_highest("iloveindiamydeard"))

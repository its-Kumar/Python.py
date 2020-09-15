"""
WAP to implement the given pattern:

 Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""

n, m = map(int, input().split())
upper = [(".|." * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
lower = upper[::-1]
print("\n".join(upper + ["WELCOME".center(m, '-')] + lower))

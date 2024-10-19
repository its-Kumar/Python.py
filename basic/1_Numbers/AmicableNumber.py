"""
Check if the given number is an amicable number or not
Amicable number: 220
sum of divisors of 220 is 284
sum of divisors of 284 is 220
"""


def divisors(num: int):
    out = []
    for i in range(1, num):
        if num % i == 0:
            out.append(i)
    return out


def amicable_number(num):
    n1 = sum(divisors(num))
    n2 = sum(divisors(n1))
    return 1 if num == n2 else 0


n = int(input())
p = amicable_number(n)
print(p)

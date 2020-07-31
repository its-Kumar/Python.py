def black_jack(a, b, c):
    if (a < 1 or a > 11) or (b < 1 or b > 11) or (c < 1 or c > 11):
        return "Number Exceeds...\n"
    s = a+b+c
    if s <= 21:
        return s
    elif s > 21:
        if a == 11 or b == 11 or c == 11:
            s -= 10
            return s
    if s > 21:
        return "BUST"


print(
    black_jack(5, 6, 7),
    black_jack(9, 9, 9),
    black_jack(9, 9, 11)
)

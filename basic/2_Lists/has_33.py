def has_33(lst):
    for i in range(len(lst) - 1):
        if lst[i + 1] == lst[i] == 3:
            return True
    return False


print(
    has_33([1, 2, 3, 4, 5]),
    has_33([1, 1, 2, 3, 4, 5, 3]),
    has_33([1, 2, 5, 3, 3]),
    has_33([3, 4, 5, 3]),
)

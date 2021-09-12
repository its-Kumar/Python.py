def summer_69(arr):
    total = 0
    add = True
    for n in arr:
        while add:
            if n != 6:
                total += n
                break
            else:
                add = False
        while not add:
            if n != 9:
                break
            else:
                add = True
                break
    return total


print(
    summer_69([1, 3, 5]),
    summer_69([4, 5, 6, 7, 8, 9]),
    summer_69([2, 1, 6, 9, 11])
)

def lesser_of_two_evens(n1, n2):
    if (n1 % 2 == 0) and (n2 % 2 == 0):
        return min(n1, n2)
    else:
        return max(n1, n2)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(5, 8))

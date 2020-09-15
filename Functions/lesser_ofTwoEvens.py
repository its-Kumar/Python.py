def lesser_ofTwoEvens(n1, n2):
    if (n1 % 2 == 0) and (n2 % 2 == 0):
        return min(n1, n2)
    else:
        return max(n1, n2)


print(lesser_ofTwoEvens(2, 4))
print(lesser_ofTwoEvens(5, 8))

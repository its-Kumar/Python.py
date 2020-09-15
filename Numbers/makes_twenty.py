def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or (n1 == 20 or n2 == 20)


print(makes_twenty(10, 20), makes_twenty(12, 8), makes_twenty(14, 18))

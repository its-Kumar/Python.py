def customegen(x, y):
    while x < y:
        yield x
        x += 1


result = customegen(25, 50)
for i in result:
    print(i)

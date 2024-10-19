def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fib()
print(type(f))

for f in fib():
    print(f)
    if f > 100:
        break

def check(a: int, b: int, c: int):
    arr = [False for i in range(c + 2)]
    if a <= c:
        arr[a] = True
    if b <= c:
        arr[b] = True
    result = 0
    c_a, c_b = a, b
    for i in range(min(a, b), c + 1):
        if arr[i]:
            if (i + a) <= c:
                arr[i + a] = True
                c_a -= i
            if (i + b) <= c:
                arr[i + b] = True
                c_b -= i
            result += 1
        return result != 0


t = int(input())
while t:
    a, b, c = [int(x) for x in input().split()]
    print("Yes") if check(a, b, c) else print("No")
    t -= 1

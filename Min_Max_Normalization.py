arr = list(map(int, input("Enter array: ").split()))
M, m = max(arr), min(arr)

i = 0
while i < len(arr):
    if arr[i] == M:
        arr[i] = 1
    elif arr[i] == m:
        arr[i] = 0
    else:
        arr[i] = (arr[i] - m) / (M - m)
    i += 1

print(arr)

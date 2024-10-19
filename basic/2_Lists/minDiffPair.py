def find_min_diff(arr):
    arr.sort()
    minDiff = 999999
    for i in range(len(arr) - 1):
        if (arr[1 + 1] - arr[i]) < minDiff:
            minDiff = arr[i + 1] - arr[i]
    return minDiff


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    minDiff = find_min_diff(arr)
    out = []
    for i in range(len(arr) - 1):
        if (arr[i + 1] - arr[i]) == minDiff:
            out += [arr[i], arr[i + 1]]
    print(" ".join([str(x) for x in out]))

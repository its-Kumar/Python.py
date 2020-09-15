def max_crossingsum(arr, l, m, h):
    sm = 0
    left_sum = -10000

    for i in range(m, l - 1, -1):
        sm += arr[i]
        if (sm > left_sum):
            left_sum = sm

    sm = 0
    right_sum = -10000
    for i in range(m + 1, h + 1):
        sm += arr[i]
        if (sm > right_sum):
            right_sum = sm

    return right_sum + left_sum


def max_subarraySum(arr, l, h):
    if (l == h):
        return arr[l]

    m = (l + h) // 2

    return max(max_subarraySum(arr, l, m), max_subarraySum(arr, m + 1, h),
               max_crossingsum(arr, l, m, h))


if __name__ == "__main__":
    arr = [int(x) for x in input("Enter elements : ").split()]
    n = len(arr)
    print("Array is ", arr)

    max_sum = max_subarraySum(arr, 0, n - 1)

    print("Maximum contigeous sum : ", max_sum)

def find_sub_array(arr: "list[int]", sum_: int):
    current_sum = 0
    left = right = 0
    n = len(arr)
    while right < n:
        if current_sum == sum_:
            print(f"Sub-array of given sum {sum_} is: ", arr[left:right])
            print("Length of sub-array is : ", right - left)
            return 1

        while current_sum > sum_ and left < right - 1:
            current_sum -= arr[left]
            left += 1
        if current_sum < sum_ and right < n:
            current_sum += arr[right]
            right += 1
    # if we reach here there is no sub-array
    return 0


if __name__ == "__main__":
    arr = list(map(int, input("Enter array:").split()))
    Sum = int(input("Enter sum: "))
    print("Array is: ", arr)
    if not find_sub_array(arr, Sum):
        print("There is no sub array of given sum", Sum)

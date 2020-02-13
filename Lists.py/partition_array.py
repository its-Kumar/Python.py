def make_partition(arr):
    """
    INPUT : array
    
    OUTPUT : array1, array2
            array1 -> partition of array
            array2 -> partition of array
            such that the absolute diffrent of sum of array1 and array2 will minimum.
    """
    arr1 = []
    arr2 = []
    for i in range(arr):
        if arr[i] not in arr1:
            arr1.append(arr[i])
        min_ = find_min(arr)
        
    return arr1,arr2


n = int(input("Enter the no of elements : "))
arr = []
for i in range(n):
    arr.append(int(input()))
print("Your array is  : ")
print(arr)
part1, part2 = make_partition(arr)
print(part1, part2)
print(sum(part1) - sum(part2))

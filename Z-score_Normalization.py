import statistics
import matplotlib.pyplot as plt
arr = list(map(int, input("Enter array: ").split()))
m = statistics.mean(arr)
sigma = statistics.stdev(arr)

i = 0
while i< len(arr):
	arr[i] = (arr[i] - m)/sigma
	i +=1

print(arr)

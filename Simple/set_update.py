# Enter your code here. Read input from STDIN. Print output to STDOUT
def command(operation):
    global a,b
    if operation == "intersection_update":
        a &=b
    elif operation =="update":
        a.update(b)
    elif operation == "symmetric_difference_update":
        a ^=b
    elif operation =="difference_update":
        a -=b
    else:
        print("Operation not found!!")

n_a = int(input())
a = set(map(int,input().split()))
n = int(input())

for _ in range(n):
    operation,n_b = input().split()
    n_b = int(n_b)
    b = set(map(int,input().split()))
    command(operation)
print(sum((a)))

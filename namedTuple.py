from collections import namedtuple

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
columns = input().split()
students = namedtuple("students", columns)
marks = [int(students._make(input().split()).MARKS) for _ in range(n)]

for i in students:
    print(i)
print(marks)
print(sum(marks) / len(marks))

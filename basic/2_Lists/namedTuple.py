from collections import namedtuple

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input("Enter n:"))
columns = input("Enter Columns: ").split()
Students = namedtuple("Students", columns)
marks = [int(Students._make(input("Enter Marks: ").split()).MARKS)
         for _ in range(n)]

# for i in Students:        # Will not work
#   print(i)

print("Marks:", marks)
print("Average:", sum(marks) / len(marks))

print("f(x) = n + nn + nnn + .........................\n")
n = int(input("Enter n : "))
t = int(input("Enter no. of terms : "))

result = 0
for i in range(t):
    result += n**(i + 1)

print("Result = ", result)

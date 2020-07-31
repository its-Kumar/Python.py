n = int(input("Enter n : "))

dict = {}
for x in range(1, n+1):
    dict.update({x: x*x})


print(dict)

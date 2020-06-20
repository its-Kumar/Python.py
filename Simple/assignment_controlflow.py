n = int(input("Input any number"))

for num in range(n+1):
    if(num % 10) == 0:
        continue
    if(num > 100):
        break
    print(num)

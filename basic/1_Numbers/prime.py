num = int(input("Enter any number : "))
primeFlag = True

for i in range(2, num):
    if (num % i) == 0:
        primeFlag = False
        break
    else:
        pass

if primeFlag:
    print(num, " is prime.")
else:
    print(num, " is not prime.")

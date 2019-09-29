number=int(input("Enter a number : "))
orignal_number =number

r=0
while(orignal_number >0):
    remainder = orignal_number % 10
    r = r +  (remainder**3)
    orignal_number //= 10
    

if r == number:
    print("Number {:d} is Armstrong".format(number))
else:
    print("Number {:d} is not  Armstrong".format(number))
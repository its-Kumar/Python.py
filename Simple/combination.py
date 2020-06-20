lst = [int(x) for x in input("Enter three digits : ").split()]
print(lst)

print("All Combinations -->\n")

for i in range(3):
    for j in range(3):
        for k in range(3):
            if(i != j and j != k and i != k):
                print(lst[i], lst[j], lst[k])

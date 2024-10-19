s = input("Enter any string  : ")
l_c, u_c, o_c = 0, 0, 0
for char in s:
    if char.islower():
        l_c += 1
    elif char.isupper():
        u_c += 1
    else:
        o_c += 1
print(f"String contains {l_c} lower, {u_c} upper and {o_c} other characters.")

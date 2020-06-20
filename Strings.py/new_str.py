str = input("Enter any string")

l = len(str)
new_str = ""
new_str += str[0]
new_str += str[1]
new_str += str[-1]
new_str += str[-2]
print(new_str)

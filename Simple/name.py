# format to print
# First name M. Last name

first_name = input("Enter your first name : ")
middle_name = input("Enter your middle name : ")
last_name = input("Enter your last name : ")

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s}. {last}"
print(name_format.format(first=first_name, middle=middle_name, last=last_name))

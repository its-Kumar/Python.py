def old_macdonals(name):
    name = name.capitalize()
    return name.replace(name[3],name[3].upper())

print(
    old_macdonals("macdonals")
)  
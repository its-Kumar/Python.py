def rotate(str):
    """
    Rotate the given string 'str'

    INPUT : "Hello"
    
    OUTPUT : "elloH"
    """
    str = list(str)
    temp = str.pop(0)
    str.append(temp)
    return "".join(str)

def string_rotations(str):
    """
    INPUT : "Hello" <String>

    OUTPUT: ['elloH', 'lloHe', 'loHel', 'oHell', 'Hello']
    """
    lst = []
    for i in range(len(str)):
        str = rotate(str)
        lst.append(str)
    return lst 



s = input("Enter any string : ")
print("You have entered : ",s)
rotations = string_rotations(s)
print("\nThe rotations are : ")
print(rotations)

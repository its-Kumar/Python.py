def rotate(string):
    """
    Rotate the given string 'str'

    INPUT : "Hello"

    OUTPUT : "elloH"
    """
    string = list(string)
    temp = string.pop(0)
    string.append(temp)
    return "".join(string)


def string_rotations(string):
    """
    INPUT : "Hello" <String>

    OUTPUT: ['elloH', 'lloHe', 'loHel', 'oHell', 'Hello']
    """
    lst = []
    for i in range(len(string)):
        string = rotate(string)
        lst.append(string)
    return lst


s = input("Enter any string : ")
print("You have entered : ", s)
rotations = string_rotations(s)
print("\nThe rotations are : ")
print(rotations)

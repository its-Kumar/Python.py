alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(s, shift=3):
    encrypted_str=""
    for char in s:
        if char ==' ':
            encrypted_str += char
        else:
            index = alpha.index(char)
            shifted_index = (index + shift) % len(alpha)
            encrypted_str += alpha[shifted_index]
    return encrypted_str

def decrypt(e, shift =3):
    decrypted_str=""
    for char in e:
        if char ==' ':
            decrypted_str += char
        else:   
            index = alpha.index(char)
            shifted_index = (index - shift) % len(alpha)
            decrypted_str += alpha[shifted_index]
    return decrypted_str

if __name__=='__main__':
    str = input("Enter msg : ")
    encrypted_msg = encrypt(str,2)
    print("encrypted msg : ",encrypted_msg)
    print("decrypted msg : ",decrypt(encrypted_msg,2))
    
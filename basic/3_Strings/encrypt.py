"""
Encryption & Decryption using `Shift Cipher`
"""


def encrypt(plain_text: str, shift: int = 3):
    encrypted_str = ""
    for char in plain_text:
        if char == " ":
            encrypted_str += char
        else:
            encrypted_str += chr((ord(char) + shift))
    return encrypted_str


def decrypt(encrypted_text: str, shift: int = 3):
    decrypted_str = ""
    for char in encrypted_text:
        if char == " ":
            decrypted_str += char
        else:
            decrypted_str += chr((ord(char) - shift))
    return decrypted_str


if __name__ == "__main__":
    s = input("Enter msg : ")
    encryption_key = int(input("Enter encryption key: "))
    encrypted_msg = encrypt(s, encryption_key)
    print("encrypted msg : ", encrypted_msg)
    print("decrypted msg : ", decrypt(encrypted_msg, encryption_key))

import sys
from os import remove


def breaker(data):
    global extension
    n = int(input("Enter the no of parts : "))
    len_ = len(data) // n
    for i in range(n):
        f_name = "part" + str(i) + "." + extension
        f = open(f_name, "w")

        f.writelines(data[len_ * i: len_ * (i + 1)])
        f.close()
    print("\nFile Break successfully..!!\n")


def joiner(files):
    global extension
    f = open("joined_file" + "." + extension, "w")
    for i in range(len(files)):
        fl = open(files[i], "r")
        data = fl.read()
        f.write(data)
        fl.close()
    print("File joined..!!")
    f.close()


def clear(f_name="part0.txt"):
    remove(f_name)


extension = ""
if __name__ == "__main__":
    while True:
        print("\t**Welcome to File Breaker**\n")
        print(
            """
        1. Break the file
        2. Join the file
        3. Clear all files
        4. Exit
        """
        )
        choice = int(input("\tEnter your choice:"))

        if choice == 1:
            file_name = input("Enter the file name : ")
            extension = file_name.split(".")[1]
            file = open(file_name, "r")
            data = file.readlines()
            breaker(data)
            file.close()

        elif choice == 2:
            print("Enter the file names to join:")
            files = input().split()
            extension = (files[0].split("."))[1]
            joiner(files)

        elif choice == 3:
            f_name = input("Enter file name : ")
            clear(f_name)
            print("files cleared..!!\n")

        elif choice == 4:
            print("\tThanks..!!\n")
            sys.exit(0)

        else:
            print("Wrong Choice..!!")

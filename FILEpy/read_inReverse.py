try:
    with open("data.txt", 'r') as f:
        line = f.read()
        line = line[::-1]
        print(line)


except FileNotFoundError:
    print("File not found ... ")


finally:
    f.close()

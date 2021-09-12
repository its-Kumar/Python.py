if __name__ == "__main__":
    x = input("Enter number 1: ")
    y = input("Enter number 2: ")
    try:
        z = int(x) / int(y)
    except Exception as e:
        print("Exception occurred ", e)
        z = None
    finally:
        print(z)

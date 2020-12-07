if __name__ == "__main__":
    x = input("Enter number 1: ")
    y = input("Enter number 2: ")
    try:
        z = x / int(y)
    except Exception as e:
        print("Exception type: ", type(e).__name__)
        print("Exception occured:", e)
        z = None
    finally:
        print(z)
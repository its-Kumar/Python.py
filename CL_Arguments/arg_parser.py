"""Using argument parser"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    # parser.add_argument("operation", help="operation")

    parser.add_argument(
        "--operation",
        help="operation",
        choices=["add", "substract", "multiply", "division"],
    )  # optional argument

    args = parser.parse_args()
    # print(args)
    print(args.number1)
    print(args.number2)
    # print(args.operation)

    result = None
    if args.operation == "add":
        result = int(args.number1) + int(args.number2)
    elif args.operation == "substract":
        result = int(args.number1) - int(args.number2)
    elif args.operation == "multiply":
        result = int(args.number1) * int(args.number2)

    elif args.operation == "division":
        result = int(args.number1) / int(args.number2)
    else:
        print("Unsupported operation")

    print("Result:", result)

import json

if __name__ == "__main__":
    with open("myjson.json", "r") as f:
        print("loading json from file......")
        s = f.read()
        print("done!!")
    print(s)
    print(type(s))
    book = json.loads(s)
    print(book)
    print(type(book))
    print(book['pop'])

"""
JSON: JavaScript Object Notation
JSON is lightweight than XML
Example:
-----------
JSON-
{
    "name" : "NAME",
    "Address" : "address............",
    .....

}

XML-
<name> NAME </name>
<address> address............</address>
.....
"""

import json

if __name__ == "__main__":
    book = {}
    book['tom'] = {
        "name": "tom",
        "address": "1 red street",
        "phone": 1234545,
    }
    book['pop'] = {
        "name": "pop",
        "address": "2 red street",
        "phone": 1245545,
    }
    print(book)
    print(type(book))
    s = json.dumps(book)
    print(s)
    print(type(s))

    # Saving to json file
    with open("myjson.json", "w") as f:
        print("saving json into file........")
        f.write(s)
        print("done!!")

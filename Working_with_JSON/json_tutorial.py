import json
from json import JSONEncoder

dct = {"name": "kumar", "age": 21, "hasChildren": False,
       "married": False, "salary": 30000}

# json string encoding
dct_json = json.dumps(dct, indent=4)
print(dct_json)

# json file encoding
with open('dct.json', 'w') as f:
    json.dump(dct, f, indent=4, sort_keys=True)


# decoding string
dct = json.loads(dct_json)
print(dct)

# decoding file
with open('dct.json', 'r') as f:
    dct = json.load(f)

print(dct)


# Encoding class object
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, "Class": obj.__class__
                .__name__}
    else:
        raise TypeError("Object of type User is not JSON serializable")


user = User(name="Kumar", age=21)
user_json = json.dumps(user, default=encode_user)
# print(user_json)


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, "Class": o.__class__
                    .__name__}
        return super().default(o)


user_json = json.dumps(user, cls=UserEncoder)
user_json = UserEncoder().encode(user)
print(user_json)


# decode object
user = json.loads(user_json)
# print(type(user))


def decode_user(dct):
    if User.__name__ in dct.values():
        return User(name=dct["name"], age=dct["age"])
    return dct


user = json.loads(user_json, object_hook=decode_user)
print(user.name, type(user))

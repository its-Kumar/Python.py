class Student:
    """Student class"""

    def __init__(self, name: str, _id=0):  # @ReservedAssignment
        assert isinstance(name, str), "name should be string"
        assert isinstance(_id, int), "id should be int"
        assert (_id >= 0), "id should not be negative"

        self.__name = name
        self.__id = _id

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def display(self):
        print(self)

    def __repr__(self):
        return f"Student(id={self.__id}, name='{self.__name}')"


s1 = Student("KUMAR", 25)
# print(s1.__id);   print(s1.__name)
s1.display()

# Name Mangling
print(s1._Student__id)
print(s1._Student__name)

s2 = Student("Shanu", 2)
s2.display()

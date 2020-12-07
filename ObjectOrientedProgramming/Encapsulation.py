class Student:
    def __init__(self, name="", id=0):  # @ReservedAssignment
        self.name = name
        self.id = id
        self.__name = name
        self.__id = id

    def display(self):
        print(self.__id, self.__name)


s1 = Student("KUMAR", 25)
# print(s1.__id);   print(s1.__name)
s1.display()

# Name Mangling
print(s1._Student__id)
print(s1._Student__name)

s2 = Student()

s2._Student__id = 23
s2._Student__name = "shanu"
s2.display()

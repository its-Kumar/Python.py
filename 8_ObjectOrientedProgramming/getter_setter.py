class Student:
    def __init__(self):
        self.__name = ""
        self.__id = 0

    def get_name(self):
        """Name getter"""
        return self.__name

    def get_id(self):
        """Id getter"""
        return self.__id

    def set_name(self, value: str):
        """name setter"""
        assert isinstance(value, str), "name should be a str"
        assert (value != ""), "name should not be empty"

        self.__name = value

    def set_id(self, value: int):
        """Id setter"""
        assert isinstance(value, int), "id should be int"
        assert value >= 0, "id should not be negative"

        self.__id = value

    def __repr__(self):
        return f"Student(id={self.__id}, name='{self.__name}')"


s1 = Student()
s2 = Student()
print(s1, s2)

s1.set_name("Kumar")
s1.set_id(1)
print(s1.get_name(), s1.get_id())

s2.set_id(3)
s2.set_name("Shanu")
print(s1, s2)

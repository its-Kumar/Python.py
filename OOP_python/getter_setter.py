class Student:

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


s1 = Student()
s2 = Student()
s1.set_id(1)
s1.set_name("Kumar")
s2.set_id(3)
s2.set_name("Shanu")
print(s1.get_id(), s1.get_name())
print(s2.get_id(), s2.get_name())

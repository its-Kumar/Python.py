class Car:

    class Engine:

        def set_engine(self, no):
            self.no = no

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color


c1 = Car("Honda Car", 2018, "red")
print(
    c1.name,
    c1.model,
    c1.color)

e1 = c1.Engine()
e1.set_engine(4)

print(e1.no)

import sys


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def substract(self):
        if self.a > self.b:
            return self.a - self.b
        else:
            return self.b - self.a

    def multiply(self):
        return self.a * self.b

    def devide(self):
        if self.b == 0:
            print("Divide by zero")
            sys.exit()
        else:
            return self.a / self.b

    def power(self):
        return self.a ** self.b


c1 = Calculator(2, 0)
print("Add : ", c1.add())
print("Sub : ", c1.substract())
print("Mul : ", c1.multiply())
print("Div : ", c1.devide())
print("Pow : ", c1.power())

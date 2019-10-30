from abc import abstractmethod
from math import pi
class Shapes:
    
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shapes):
    
    def __init__(self,height, width):
        self.height =height
        self.width = width
        
    def area(self):
        return self.height * self.width
    
class Circle(Shapes):
    
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return pi*self.radius *self.radius
    
    def perimeter(self):
        return (2 *pi *self.radius)
    
class Triangle(Shapes):
    
    def __init__(self,base, height):
        self.base = base
        self.height =height
        
    def area(self):
        return (1/2)*self.base* self.height
    


if __name__ == "__main__":
    r = Rectangle(3,4)
    c = Circle(2)
    t = Triangle(2,3)
    
    print("Area of ")
    print("Rectangle : ",r.area())
    print("Circle : ",c.area())
    print("Triangle : ",t.area())
    print("Parimeter of circle ",c.perimeter())

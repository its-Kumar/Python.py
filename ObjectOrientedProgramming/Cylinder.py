class Cylinder:

    pi = 3.1416

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.radius * self.radius

    def surface_area(self):
        return (2 * Cylinder.pi * self.radius * (self.height + self.radius))


C = Cylinder(height=3, radius=2)

print(C.surface_area(), C.volume())

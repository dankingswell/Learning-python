class Sphere():
    Pi = 3.14
    def __init__(self,radius):
        self.Radius = radius
        self.Diameter = radius *2

    def surfaceArea(self):
        return (4* self.Pi) * (self.Radius**2)

    def volume(self):
        return 4/3 * (self.Pi * (self.Radius**3))


s = Sphere(2)
print(s.volume())
print(s.surfaceArea())
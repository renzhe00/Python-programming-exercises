class Circle():
    def __init__(self, radius):
        self.PI = 3.14
        self.radius = radius
    
    def area(self):
        return self.radius**2*self.PI

aCircle = Circle(3)
print(aCircle.area())
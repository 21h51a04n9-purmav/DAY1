class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
shape=Square(2)
circle=Circle(3)
print(shape.area())
print(circle.area())

    

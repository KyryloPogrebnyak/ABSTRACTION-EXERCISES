from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
rectangle = Rectangle(5,10)
circle = Circle(5)

print(f"Area of rectangle is: {rectangle.area()}")
print(f"Area of circle is: {circle.area()}")

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Drawable):
    def draw(self):
        print("Drawing rectangle")

class Circle(Drawable):
    def draw(self):
        print("Drawing circle")

rectangle = Rectangle()
circle = Circle()

rectangle.draw()
circle.draw()

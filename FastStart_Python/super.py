class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        self.area = self.width * self.height
        return self.area

class Square(Rectangle):
    def __init__(self, s):
        super().__init__( s, s)

class Cube(Square):

    def area(self):
        return super().area() * 6

    def volume(self):
        return self.width ** 3

cu = Cube(5)
print(cu.area())
print(cu.volume())

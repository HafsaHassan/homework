import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta


@abc.abstractmethod
def calc_perimeter(self, input):
    """Method documentation"""
    return


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim


class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = self.a + self.b
        print("Consider me implemented", perim)
        return perim


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)


triangle = Triangle(1, 2, 3)
triangle.calc_perimeter()

rectangle = Rectangle(2, 3)
rectangle.calc_perimeter()

square = Square(2)
square.calc_perimeter()

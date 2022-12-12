from math import pi

class Color():
    def __init__(self, color):
        self.color = color


class Rectangle():
    name = "Прямоугольник"
    def __init__(self, height = 1, width = 2, color="без цвета"):
        self.height = height
        self.width = width
        self.color = color
    
    def space(self):
        return self.height * self.width
    
    def __repr__(self):
        return ("{} {} на {}, цвета \"{}\", площадью {}".format(
            self.name, self.height, self.width, self.color, self.space()
        ))

class Circle():
    name = "Круг"
    def __init__(self, radius = 1, color = "без цвета"):
        self.radius = radius
        self.color = color
    
    def space(self):
        return pi * (self.radius**2)
    
    def __repr__(self):
        return ("{} радиуса {}, цвета \"{}\", площадью {}".format(
            self.name, self.radius, self.color, self.space()
        ))

class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, width, color="без цвета"):
        super().__init__(width, width, color)
    
    

circle_example = Rectangle(10, 2,"красный")
print(circle_example)


from random import randint
from time import sleep

class Point():
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, x):
        self.__y = y


class Segment():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Figure():
    def __init__(self):
        self.__points = []
        self.segments = []

    def add_point(self, *points):
        for point in points:
            self.__points.append(point)

    def add_segment(self, *segments):
        for segment in segments:
            self.segments.append(segment)

    def is_point_in(self, P1):
        while True:
            count = 0
            for segment in self.segments:
                M1 = segment.a
                M2 = segment.b
                t_x = randint(-1000, 1000)
                sleep(1)
                t_y = randint(-1000, 1000)
                P2 = Point(t_x, t_y)
                x0 = P1.x
                y0 = P1.y
                v = P2.x - P1.x
                w = P2.y - P1.y

                a = M2.y - M1.y
                b = M1.x - M2.x

                c = -M1.x * M2.y + M1.y * M2.x
                t = (-a * x0 - b * y0 - c) / (a * v + b * w)

                if t >= 0:
                    x =P1.x + v * t
                    y = P1.y + w * t
                    segment_mod = round(((segment.a.x - segment.b.x) ** 2 + (segment.a.y - segment.b.y)**2)**0.5, 2)
                    a =  round(((segment.a.x - x) ** 2 + (segment.a.y - y)**2)**0.5, 2)
                    b =  round(((segment.b.x - x) ** 2 + (segment.b.y - y)**2)**0.5, 2)
                    if a + b == segment_mod:
                        count += 1
            if count != 0:
                if count % 2 == 0:
                    return False
                else:
                    return True

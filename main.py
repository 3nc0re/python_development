# Задача 1. Геометричні фігури.
#
# Створіть базовий клас "Фігура", який містить методи для обчислення площі та периметру фігури.
# Створіть класи "Прямокутник", "Круг" та "Трикутник", які успадковуються від класу
# "Фігура" і мають свої власні методи для обчислення площі та периметру.

import math
class Shape:
    def perimeter(self):
        pass
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a+b < c or a+c < b or b+c < a:
            raise ValueError
    def perimeter(self):
        p = self.a+self.b+self.c
        return p
    def area(self):
        hp = self.perimeter()/2
        ar = (hp*(hp-self.a)*(hp-self.b)*(hp-self.c))**0.5
        return ar

t = Triangle(3, 10, 9)
print(t.perimeter(), t.area())

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        p = (self.a+self.b)*2
        return p
    def area(self):
        ar = self.a * self.b
        return ar

t = Rectangle(10, 5)
print(t.perimeter(), t.area())

class Square(Rectangle):
    def __init__(self, a):
        self.a = a
        self.b = a
t = Square(8)
print(t.perimeter(), t.area())

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        p = 2*math.pi*self.r
        return p
    def area(self):
        ar = math.pi*self.r*self.r
        return ar
t = Circle(7)
print(t.perimeter(), t.area())








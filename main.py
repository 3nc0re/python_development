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







#                                                   Lesson 3 Homework
# Task 1
#
# String manipulation
#
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
#
# Sample String: 'helloworld'
#
# Expected Result : 'held'
#
# Sample String: 'my'
#
# Expected Result : 'mymy'
#
# Sample String: 'x'
#
# Expected Result: Empty String
#
# Tips:
#
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing to get the last characters

string1 = 'helloworld'
string2 = 'my'
string3 = 'x'

if len(string1) < 2:
    print('')
else:
    print(string1[:2] + string1[-2:])

if len(string2) < 2:
    print('')
else:
    print(string2[:2] + string2[-2:])

if len(string3) < 2:
    print('')
else:
    print(string3[:2] + string3[-2:])


# Task 2
#
# The valid phone number program.
#
# Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.

input_number = input('Please, write a phone number: ')

if not input_number.isdigit():
    print('That is not a phone number!')
elif len(input_number) != 10:
    print('There must be 10 symbols)')
else:
    print('We will call you soon!')

# Task 3
#
# The math quiz program.
#
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.

answer = input('Let`s play a quiz. How much is 234*46? ')

if not answer.isdigit():
    print('Only numbers please')
elif answer != 10764:
    print('Not correct answer')
else:
    print('Greetings! It`s correct answer')


# Task 4
#
# The name check.
#
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The program should check if your input is equal to the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.

name = 'oleh'
name1 = input('Please write your name: ')

if name1.lower() == name:
    print(True)
else:
    print(False)

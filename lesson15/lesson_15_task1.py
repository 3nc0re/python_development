# School
#
# Make a
#
#
# class structure in python representing people at school.Make a base class called Person, a class called Student, and another one called Teacher.Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not.For example, the name should be a Person attribute, while salary should only be available to the teacher.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def talk(self):
        return f"Hello, my name is {self.name} and I’m {self.age} years old"

class Student(Person):
    def __init__(self, year, timetable, marks, name, age, gender):
        super().__init__(name, age, gender)
        self.year = year
        self.timetable = timetable
        self.marks = marks
        return f"Hello, my name is {self.name} and my marks are {self.marks}. I have {self.timetable} lessons per week"


class Teacher(Person):
    def __init__(self, salary, subject, name, age, gender):
        super().__init__(name, age, gender)
        self.salary = salary
        self.subject = subject
        return f"Hello, my name is {self.name} and my salary is {self.salary}. I teach {self.subject}"
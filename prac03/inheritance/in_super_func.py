class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

s = Student("Ali")
print(s.name)




class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)

c = Car(120)
print(c.speed)




class Animal:
    def __init__(self, kind):
        self.kind = kind

class Dog(Animal):
    def __init__(self, kind):
        super().__init__(kind)

d = Dog("Mammal")
print(d.kind)




class Book:
    def __init__(self, title):
        self.title = title

class Textbook(Book):
    def __init__(self, title):
        super().__init__(title)

b = Textbook("Physics")
print(b.title)

#5
class City:
    def __init__(self, name):
        self.name = name

class Capital(City):
    def __init__(self, name):
        super().__init__(name)

c = Capital("Astana")
print(c.name)
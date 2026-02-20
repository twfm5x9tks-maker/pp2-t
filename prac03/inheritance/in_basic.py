#1
class Animal:
    def sound(self):
        return "Sound"

class Dog(Animal):
    pass

d = Dog()
print(d.sound())

#2
class Vehicle:
    def move(self):
        return "Moving"

class Car(Vehicle):
    pass

c = Car()
print(c.move())

#3
class Person:
    def speak(self):
        return "Speaking"

class Student(Person):
    pass

s = Student()
print(s.speak())

#4
class Shape:
    def draw(self):
        return "Drawing"

class Circle(Shape):
    pass

x = Circle()
print(x.draw())

#5
class Device:
    def power(self):
        return "On"

class Phone(Device):
    pass

p = Phone()
print(p.power())
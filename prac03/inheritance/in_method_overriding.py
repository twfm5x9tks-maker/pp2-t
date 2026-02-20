class Animal:
    def sound(self):
        return "Sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

d = Dog()
print(d.sound())



class Vehicle:
    def move(self):
        return "Moving"

class Car(Vehicle):
    def move(self):
        return "Driving"

c = Car()
print(c.move())




class Person:
    def role(self):
        return "Human"

class Teacher(Person):
    def role(self):
        return "Teacher"

t = Teacher()
print(t.role())




class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4 * 4

s = Square()
print(s.area())

#5
class Device:
    def power(self):
        return "On"

class Laptop(Device):
    def power(self):
        return "Laptop On"

l = Laptop()
print(l.power())
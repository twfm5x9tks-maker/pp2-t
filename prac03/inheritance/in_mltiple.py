class A:
    def show(self):
        return "A"

class B:
    def display(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.show(), c.display())




class Fly:
    def action(self):
        return "Flying"

class Swim:
    def move(self):
        return "Swimming"

class Duck(Fly, Swim):
    pass

d = Duck()
print(d.action(), d.move())




class Writer:
    def write(self):
        return "Writing"

class Reader:
    def read(self):
        return "Reading"

class Student(Writer, Reader):
    pass

s = Student()
print(s.write(), s.read())




class Engine:
    def start(self):
        return "Start"

class Wheel:
    def roll(self):
        return "Roll"

class Car(Engine, Wheel):
    pass

c = Car()
print(c.start(), c.roll())




class Math:
    def calc(self):
        return "Math"

class Physics:
    def calc2(self):
        return "Physics"

class Science(Math, Physics):
    pass

s = Science()
print(s.calc(), s.calc2())
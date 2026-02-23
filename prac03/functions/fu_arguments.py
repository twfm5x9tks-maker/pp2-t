def my_f(name):
    print("Hello, ", name)
my_f("Valery")
my_f("Elias")
my_f("Alex")


def my_f(fname, lname):
    print(fname + " " + lname)
my_f("Lou", "Gousness")


def m_f(name = "friend"):
    print("Hi", name)
m_f("Anna")
m_f()

def my_function(animal, name):
  print("I love my", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "cat", name = "Barbara")
my_function(name = "Barbara", animal = "cat")
my_function("Barbara", "cat")

def my(people, name, age):
    print("I have a", age, "years old", people, "named", name)
my("sister", name = "Adiya", age = 14)


def fru(fruits):
    for fruit in fruits:
        print(fruit)
my_fru = ["banana", "cherry", "orange"]
fru(my_fru)


def info(person):
    print("name:", person["name"])
    print("age:", person["age"])
person = {"name": "Lou", "age": 17}
info(person)
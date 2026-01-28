# python HOME

print("Hello,professor")
print("hi")
print("Python")


# python SYNTAX

if 7<9:
    print("Nine is greater than seven!")

if 7<9:
        print("Nine is greater than seven!")


# python STATEMENTS

print("HELLO!")
print("Have a good day.")
print("Bye!")

print("HELLO!"); print("Have a good day."); print("Bye!")
print("I'm learning Python"); print("this will work")


# python OUTPUT TEXT 

print('Hello!')
print("I'm learning Python.")
print('This will work', end=" ")

# python OUTPUT NUMBERS

print(6523)
print(23+465132)
print(45*465)

print("I am", 17, "years old.")


# python VARIABLES

a=5
b="Adi"
print(a)
print(b)

a=5       #int
a="Adi"   #str
print(a)

x=str(3)   #'3'
y=int(3)   #3
z=float(3) #3.0

x=5
y="Adina"
print(type(x))
print(type(y))

x="John"
x='John' # is the same as

a=5
A="sally" # A will not overwrite a

# python NAMES

myvar = "aa"
my_var = "aa"
_my_var = "aa"
myVar = "aa"
MYVAR = "aa"
myvar2 = "aa"


# python MULTIPLE VALUES

x, y, z="banana", "apple", "cherry"
print(x)
print(y)
print(z)

x=y=z="orange"
print(x)
print(y)
print(z)

fruits= ["apple", "banana", "cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)


# python OUTPUT VARIABLES

a="Python"
print(a)

x="I am"
y="22"
z="years old"
print(x,y,z)

x="I am"
y="22"
z="years old"
print(x+y+z)

x=8
y=9
print(x+y)

x=8
y="John"
print(x, y) # if use + it is an error

# python GLOBAL VARIABLES

x="fantastic"
def my():
    print('Paris is'+x)
my()

x="amazing"
def fun():
    x="fantastic"
    print("Python is"+x)
fun()

x="amazing"
def fun():
    global x
    x="fantastic"
fun()
print("python is"+x)

# python DATA TYPES 

x = "Hello World"	                #str	
x = 20	                            #int	
x = 20.5	                        #float	
x = 1j	                            #complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	                    #range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                        #bool	
x = b"Hello"	                    #bytes	
x = bytearray(5)	                #bytearray	
x = memoryview(bytes(5))	        #memoryview	
x = None	                        #NoneType

# python NUMBERS 

x = 523                # int
y = 24512.86532        # float
z = 752j               # complex

x = 8    # int
y = 9.4  # float
z = 2j   # complex

#int to float:
a = float(x)

#float to int:
b = int(y)

#int to complex:
c = complex(x)


# python CASTING

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# python STRINGS
print("String")
print('String')

print("I'm agree")
print("He is called 'Ali'")
print('He is called "Ali"')

a="Hi"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a="Hello, World!"
print(a[1])   #e

for i in "Sunday":
    print(i)

a="run"
print(len(a)) #3

txt="I didn't go to the school"
print("didn't" in txt)  #True

txt="I'm tired"
if "tired" in txt:
    print("Yes, 'tired' is present")

txt = "I didn't go to the school"
print("want" not in txt)

txt = "I didn't go to the school"
if "want" not in txt:
  print("No, 'want' is NOT present")

# python SLICING STRINGS

c="Hello, Anna"
print(c[7:10])   #Ann
print(c[:5])     #Hello
print(c[8:])     #nna
print(c[-5:-1])  # Ann

# python MODIFY STRINGS

c="    Hello, Anna    "
print(c.upper())  #HELLO, ANNA
print(c.lower())  #hello, anna
print(c.strip())  #"Hello, Anna"
print(c.replace("A", "N"))  # Hello, Nnna
print(c.split(","))         # ['Hello', 'Anna']

# python STRING CONCATENATION

a="Hello"
b="Anna"
c=a+b
print(c)    #HelloAnna
c=a+" "+b
print(c)    #Hello Anna
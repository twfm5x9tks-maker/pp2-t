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

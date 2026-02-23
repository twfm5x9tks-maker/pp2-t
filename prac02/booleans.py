print(6>90)    #False
print(6==7)    #False
print(80<98)   #True

a=8
b=6
if a<b:
    print("b is greater than a")
else:
    print("b isn't greater than a")
# a is greater than b

print(bool("hello")) # True
print(bool(15))      # True

x="HI"
y=85
print(bool(x))     # True
print(bool(y))     # True

bool("qwerty")
bool(864513)
bool(["hi", "hello", "hola"]) # any string, number (except 0), list, tuple, set and dictionary are TRUE

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})         # There are not many values that evalute to FALSE

def myf() :
  return True
if myf():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))
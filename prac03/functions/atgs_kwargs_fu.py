def my(*kids):
  print("The eldest child is " + kids[1])
my("Lou", "Omar", "Charly")

def my_func(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_func("Lou", "Omar", "Charly")


def my_f(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_f(1, 2, 3))
print(my_f(10, 20, 30, 40))
print(my_f(5))
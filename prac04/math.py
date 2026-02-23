# math.py

import math
import random

# Built-in functions
print("Min:", min(3, 7, 1))
print("Max:", max(5, 9, 2))
print("Abs:", abs(-10))
print("Round:", round(3.6))
print("Power:", pow(2, 3))

# math module
print("Sqrt:", math.sqrt(16))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.9))
print("Sin(pi/2):", math.sin(math.pi / 2))
print("Cos(0):", math.cos(0))
print("Pi:", math.pi)
print("Euler number:", math.e)

# random module
print("Random float:", random.random())
print("Random int:", random.randint(1, 10))
print("Random choice:", random.choice([1, 2, 3, 4, 5]))

lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print("Shuffled list:", lst)
# Examples of map, filter, reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: multiply each element by 2
doubled = list(map(lambda x: x*2, numbers))
print("Doubled:", doubled)

# filter: select even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce: sum all elements
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)
from functools import reduce

nums = [1, 2, 3, 4, 5]

#1
print(list(map(lambda x: x**2, nums)))


#2
print(list(map(str, nums)))


#3
print(list(filter(lambda x: x % 2 == 0, nums)))


#4
print(list(filter(lambda x: x > 2, nums)))


#5
print(reduce(lambda x, y: x*y, nums))
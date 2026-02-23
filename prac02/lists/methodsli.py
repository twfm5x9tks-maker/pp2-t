# append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# clear()
my_list.clear()
print(my_list)

# copy()
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)
print(original)
print(copy_list)

# count()
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))

# extend()
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print(list_a)

# index()
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))

# insert()
numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)

# pop()
items = [10, 20, 30, 40]
removed = items.pop()
print(removed)
print(items)

# remove()
colors = ["red", "blue", "green", "blue"]
colors.remove("blue")
print(colors)

# reverse()
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)

# sort()
data = [5, 1, 4, 2, 3]
data.sort()
print(data)

# sort reverse
data.sort(reverse=True)
print(data)

# sort by length
words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print(words)
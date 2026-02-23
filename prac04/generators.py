# generators.py

# -------- Iterator --------

class MyIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        else:
            raise StopIteration


it = MyIterator(5)
print("Iterator output:")
for x in it:
    print(x)


# -------- Generator Function --------

def my_generator(n):
    for i in range(1, n + 1):
        yield i


print("\nGenerator output:")
for x in my_generator(5):
    print(x)


# -------- Generator Expression --------

gen = (x * x for x in range(1, 6))

print("\nGenerator expression output:")
for x in gen:
    print(x)
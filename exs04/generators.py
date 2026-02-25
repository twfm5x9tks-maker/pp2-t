#1

def generate_squares(N):
    """Generator to yield squares from 0 to N-1"""
    for i in range(N):
        yield i ** 2

N = 5
for square in generate_squares(N):
    print(square, end=", ")



#2
def even_numbers(n):
    """Generator to yield even numbers from 0 to n"""
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))
print(", ".join(str(num) for num in even_numbers(n)))



#3
def divisible_by_3_and_4(n):
    """Generator to yield numbers divisible by both 3 and 4"""
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 50
for num in divisible_by_3_and_4(n):
    print(num, end=", ")


#4
def squares(a, b):
    """Generator to yield squares of numbers from a to b inclusive"""
    for i in range(a, b + 1):
        yield i ** 2

for val in squares(3, 7):
    print(val, end=", ")



#5
def countdown(n):
    """Generator to yield numbers from n down to 0"""
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num, end=", ")
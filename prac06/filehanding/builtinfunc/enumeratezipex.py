names = ["Ali", "Aruzhan", "Dias"]
scores = [80, 90, 70]

#1
for i, name in enumerate(names):
    print(i, name)


#2
for i, name in enumerate(names, start=1):
    print(i, name)


#3
for n, s in zip(names, scores):
    print(n, s)


#4
print(list(zip(names, scores)))


#5
print(int("10"))
print(float("5.5"))
print(len(names))
print(max(scores))
print(sorted(scores))
# Examples of enumerate and zip
names = ["Ali", "Aisha", "Enlik"]
scores = [90, 85, 100]

# enumerate: index and element
for index, name in enumerate(names, start=1):
    print(index, name)

# zip: pair two lists
for name, score in zip(names, scores):
    print(f"{name} score: {score}")
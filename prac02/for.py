numbers = [2, 8, 52]
for i in numbers: 
    print(i)

for i in "hello":
    print(i)

for i in numbers:
    print(i)
    if i==8:
        break


fruits = ["cherry", "apple", "banana"]
for x in fruits:
  if x == "banana":
    break
  print(x)

for x in fruits:
  if x == "banana":
    continue
  print(x)

for i in range(9):
   print(i)

for i in range(9,19):
   print(i)

for i in range(9,19,3):
   print(i)


for x in range(10):
  print(x)
else:
  print("Finally finished!")


for x in range(10):
  if i==5:break
  print(x)
else:
  print("Finally finished!")


for i in numbers:
   for j in fruits:
      print(i,j)
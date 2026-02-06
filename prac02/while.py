x = 2
while x < 6:
  print(x)
  x += 1


while x < 6:
  print(x)
  if x == 3:
    break
  x += 1

while x < 6:
  x += 1
  if x == 3:
    continue
  print(x)

while x < 8:
  print(x)
  x += 1
else: 
  print("x is no longer lass than 8")
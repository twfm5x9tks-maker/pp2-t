a = 27
b = 15
c = 76
if a > b and c > a:
  print("Both conditions are True")


a = 27
b = 15
c = 76
if a > b or a > c:
  print("At least one of the conditions is True")


a = 10
b = 289
if not a > b:
  print("a is NOT greater than b")


username = "Aya"
password = "qwet123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
import re

# 1
pattern1 = r"ab*"
print("1:", bool(re.fullmatch(pattern1, "a")))
print("1:", bool(re.fullmatch(pattern1, "abbb")))

# 2.
pattern2 = r"ab{2,3}"
print("2:", bool(re.fullmatch(pattern2, "abb")))
print("2:", bool(re.fullmatch(pattern2, "abbb")))
print("2:", bool(re.fullmatch(pattern2, "abbbb")))

# 3
text3 = "hello_world test_string wrong-Format"
pattern3 = r"\b[a-z]+_[a-z]+\b"
print("3:", re.findall(pattern3, text3))

# 4
text4 = "Hello World ABC Test"
pattern4 = r"\b[A-Z][a-z]+\b"
print("4:", re.findall(pattern4, text4))

# 5
pattern5 = r"a.*b"
print("5:", bool(re.fullmatch(pattern5, "axxxb")))
print("5:", bool(re.fullmatch(pattern5, "ab")))

# 6
text6 = "Hello, world. Python is fun"
result6 = re.sub(r"[ ,\.]", ":", text6)
print("6:", result6)

# 7
def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

print("7:", snake_to_camel("hello_world_test"))

# 8
text8 = "HelloWorldTest"
result8 = re.findall(r"[A-Z][^A-Z]*", text8)
print("8:", result8)

# 9
text9 = "HelloWorldTest"
result9 = re.sub(r"([A-Z])", r" \1", text9).strip()
print("9:", result9)

# 10
def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower().lstrip("_")

print("10:", camel_to_snake("HelloWorldTest"))
# Example of writing and appending to a file
from pathlib import Path

file_path = Path("sample.txt")

# Write: overwrite file content
with open(file_path, "w") as file:
    file.write("This is the first line\n")
    file.write("This is the second line\n")

# Append: add new line to the end
with open(file_path, "a") as file:
    file.write("This is an appended line\n")

# Show the result
with open(file_path, "r") as file:
    print(file.read())
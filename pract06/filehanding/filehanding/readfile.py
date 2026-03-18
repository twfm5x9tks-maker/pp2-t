# Example of reading data from a file
from pathlib import Path

file_path = Path("sample.txt")

# Read entire file
with open(file_path, "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Read one line
with open(file_path, "r") as file:
    first_line = file.readline()
    print("First line:", first_line)

# Read all lines as a list
with open(file_path, "r") as file:
    lines = file.readlines()
    print("All lines:", lines)
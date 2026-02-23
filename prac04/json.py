# json.py

import json

# Python -> JSON
data = {
    "students": [
        {"name": "Ali", "age": 18},
        {"name": "Aruzhan", "age": 17}
    ]
}

json_string = json.dumps(data, indent=4)
print("JSON string:\n", json_string)

# Write JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("\nLoaded JSON data:")
for student in loaded_data["students"]:
    print(student["name"], student["age"])
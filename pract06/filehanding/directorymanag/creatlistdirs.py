# Creating directories and listing files
import os
from pathlib import Path

# Create new directories
os.makedirs("data/subfolder", exist_ok=True)

# List all files and folders in the current directory
print("Current directory contents:", os.listdir())

# Create a new file
file_path = Path("data/sample_file.txt")
file_path.write_text("File content in directory\n")
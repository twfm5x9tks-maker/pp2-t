# Moving files between directories
import shutil
from pathlib import Path

source = Path("data/sample_file.txt")
destination = Path("data/subfolder/sample_file.txt")

# Move file
shutil.move(source, destination)
print(f"{source} has been moved to {destination}.")

# List all files in subfolder
print("Files in subfolder:", list(Path("data/subfolder").iterdir()))
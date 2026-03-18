# Copying and deleting files
import shutil
from pathlib import Path

source = Path("sample.txt")
backup = Path("backup_sample.txt")

# Copy file
shutil.copy(source, backup)
print(f"{source} copied as {backup}.")

# Delete file
backup.unlink()
print(f"{backup} has been deleted.")
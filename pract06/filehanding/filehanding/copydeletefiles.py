import shutil
import os

#1
shutil.copy("file1.txt", "copy1.txt")

#2
shutil.copy2("file2.txt", "copy2.txt")

#3
shutil.copy("file3.txt", "backup_file3.txt")

#4
if os.path.exists("copy1.txt"):
    os.remove("copy1.txt")

#5
file_name = "copy2.txt"
if os.path.exists(file_name):
    os.remove(file_name)
    print("Deleted:", file_name)
else:
    print("File not found")
print("5 copy/delete examples done")
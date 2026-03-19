import shutil

#1
shutil.move("file1.txt", "folder1/file1.txt")


#2
shutil.copy("file2.txt", "folder1/file2.txt")


#3
shutil.move("file3.txt", "file3_renamed.txt")


#4
shutil.copy("file4.txt", "parent1/file4.txt")


#5
shutil.copy("file5.txt", "folder1/file5.txt")
print("5 move/copy examples done")
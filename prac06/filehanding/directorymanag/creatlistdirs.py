import os

#1
os.mkdir("folder1")


#2
os.makedirs("parent1/child1")


#3
print(os.getcwd())


#4
print(os.listdir())


#5
os.chdir("folder1")
print("Changed dir:", os.getcwd())
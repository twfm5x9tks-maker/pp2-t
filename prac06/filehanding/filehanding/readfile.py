#1
with open("filer.txt", "r") as f:
    print(f.read())


#2
with open("filer02.txt", "r") as f:
    print(f.readline())


#3
with open("filer02.txt", "r") as f:
    print(f.readlines())


#4
with open("filer03.txt", "r") as f:
    for line in f:
        print(line.strip())


#5
with open("filer3.txt", "r") as f:
    print(f.read(5)) 
print("5 read examples done")
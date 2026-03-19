#1
with open("filew01.txt", "w") as f:
    f.write("Hello World\n")


#2
with open("filew02.txt", "w") as f:
    f.write("line number1\n")
    f.write("line number2\n")
    f.write("line number2\n")


#3
lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open("filew03.txt", "w") as f:
    f.writelines(lines)


#4
number = 123
with open("filew04.txt", "w") as f:
    f.write(str(number))


#5
text = input("Enter text: ")
with open("filew05.txt", "w") as f:
    f.write(text)
print("5 write examples done")
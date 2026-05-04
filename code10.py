student = {
    "name": "Bao",
    "age": 19,
    "major": "Ai engineer"
}

file = open("student.txt", "w")

file.write("Name:" + student["name"].upper())
file.write("\n")

file.write("Age:" + str(student["age"]))
file.write("\n")

file.write("Major:" + student["major"])

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()


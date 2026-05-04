file = open("study.txt", "w")

file.write("I am learning Python")

file.close()

file = open("study.txt", "a")

file.write("\nDay 2 ")

file = open("study.txt", "r")

content = file.read()

print(content)

file.close 
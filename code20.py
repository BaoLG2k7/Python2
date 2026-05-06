x = "education"

count = 0

for i in x:
    if i not in "auieo": # not in và != là 2 khái niệm khác nhau 
        count += 1

print(count)
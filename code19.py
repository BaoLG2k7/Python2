x = "education"

count = 0 

for i in x:
    if i in "aeiou": # i duyệt qua những chữ này(nguyên âm)
        count += 1

print(count)
n = int(input("Nhập số n: "))
a = []

for i in range(n):
    a.append(int(input("Nhập số thứ {i + 1}:")))

print("Dãy số trước khi sắp xếp là:", a)

for i in range(n-1):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            a[1], a[j] = a[j], a[i]

print("Dãy sau khi sắp xếp:", a)
n = int(input("Nhập số n:"))

count = 0 

for i in range(1, n + 1, 2):
    if i <= 0:
        count += 1 
print("Số lượng số âm là:", count)
10
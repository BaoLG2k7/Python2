nums = [4, 1, 8, 2, 6]

count = 0

largest = nums[0]

for i in nums:
    if i % 2 == 0:
        print("Các số chẵn trong list:", i)
        count += 1
    if i > largest:
        largest = i 

print(f"Tổng có {count} số chẵn") # f cho phép biến vào trong chuỗi {}
print(largest)




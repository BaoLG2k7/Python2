nums = [3, 7, 2, 9, 7, 5]

print("Số đứng đầu list", nums[-1]) #(nums[-1]) flex hơn
print("Số đứng cuối list", nums[5])
print("Độ dài list là:", len(nums))
total = 0
for i in nums:
    total = total + i

print("Tổng các số trong list là:", total)


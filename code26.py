nums = [2,4,5,6,7]

target = 9

def total_nums():
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(total_nums())


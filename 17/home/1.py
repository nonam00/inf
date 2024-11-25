nums = [int(x) for x in open("1.txt")]
mn = min(x for x in nums if (100 <= abs(x) <= 999) and (abs(x) % 10 == 3))
arr = []
for i in range(len(nums) - 1):
    if (1000 <= abs(nums[i]) <= 9999)+ (1000 <= abs(nums[i+1]) <= 9999) == 1:
        if (nums[i] ** 2 + nums[i+1] ** 2) % mn == 0:
            arr.append(nums[i] ** 2 + nums[i+1] ** 2)    
print(len(arr), max(arr))

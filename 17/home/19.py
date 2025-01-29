nums = [int(i) for i in open('19.txt')]
mx = max(i for i in nums if 100 <= abs(i) <= 999)
arr = []
for i in range(len(nums) - 1):
    if (100 <= abs(nums[i]) <= 999) + (100 <= abs(nums[i + 1]) <= 999) == 1:
        sm = nums[i] + nums[i + 1]
        if sm <= mx:
            arr.append(sm)
print(len(arr), max(arr))

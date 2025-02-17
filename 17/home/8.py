nums = [int(s) for s in open('8.txt')]
arr = []
mx = max([i for i in nums if 100 <= abs(i) <= 999])
for i in range(len(nums) - 1):
    if (100 <= abs(nums[i]) <= 999) + (100 <= abs(nums[i + 1]) <= 999) == 1:
        sm = nums[i] + nums[i + 1]
        if sm <= mx:
            arr.append(sm)
print(len(arr), max(arr))
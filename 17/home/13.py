nums = [int(s) for s in open('13.txt')]
arr = []
mn = min(abs(i) for i in nums)
for i in range(len(nums) -1):
    if (nums[i] < 0) + (nums[i + 1] < 0) == 1:
        sm = nums[i] + nums[i + 1]
        if sm >= 0 and sm % mn == 0:
            arr.append(sm)
print(len(arr), max(arr))
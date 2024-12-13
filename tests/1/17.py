nums = [int(s) for s in open('17.txt')]
mx = max(x for x in nums if x % 100 == 15)
arr = []
for i in range(len(nums) - 2):
    if ((len(str(nums[i])) == 4) + (len(str(nums[i + 1])) == 4) + (len(str(nums[i + 2])) == 4)) == 1:
        sm = nums[i] + nums[i + 1] + nums[i+2]
        if sm >= mx:
            arr.append(sm)
print(len(arr), max(arr))
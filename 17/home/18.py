nums = [int(i) for i in open('18.txt')]
mx = max(i for i in nums if i % 100 == 15)
arr = []
for i in range(len(nums) - 2):
    if (1000 <= nums[i] <= 9999) + (1000 <= nums[i + 1] <= 9999) + (1000 <= nums[i + 2] <= 9999) == 1:
        sm = nums[i] + nums[i + 1] + nums[i + 2]
        if sm >= mx:
            arr.append(sm)
print(len(arr), max(arr))

nums = [int(s) for s in open('2.txt')]
mx = max(i for i in nums if 10 <= i <= 99)
arr = []
for i in range(len(nums) - 1):
    if (10 <= nums[i] <= 99) + (10 <= nums[i + 1] <= 99) == 1:
        sm = nums[i] + nums[i + 1]
        if sm % mx == 0:
            arr.append(sm)
print(len(arr), max(arr))
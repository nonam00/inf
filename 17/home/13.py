nums = [int(i) for i in open('13.txt')]
mn = min(i for i in nums if 100 <= i <= 999 and i % 10 == 3)
arr = []
for i in range(len(nums) - 1):
    if (1000 <= nums[i] <= 9999) + (1000 <= nums[i + 1] <= 9999) == 1:
        sm = nums[i] ** 2 + nums[i + 1] ** 2
        if sm % mn == 0:
            arr.append(sm)
print(len(arr), max(arr))

nums = [int(s) for s in open('10.txt')]
arr = []
mn = min(i for i in nums if 100 <= abs(i) <= 999 and abs(i) % 10 == 3)
for i in range(len(nums) - 1):
    if (1000 <= abs(nums[i]) <= 9999) + (1000 <= abs(nums[i + 1]) <= 9999) == 1:
        sm = nums[i] ** 2 + nums[i + 1] ** 2
        if sm % mn == 0:
            arr.append(sm)
print(len(arr), max(arr))
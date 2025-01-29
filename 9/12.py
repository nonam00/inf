def check(nums):
    prevd = nums[1] - nums[0]
    for i in range(2, len(nums)):
        tmp = nums[i] - nums[i - 1]
        if tmp != prevd:
            return False
        prevd = tmp
    return True
count = 0
for line in open('12.txt'):
    nums = [int(i) for i in line.split()]
    if len(nums) != len(set(nums)) or check(sorted(nums)):
        count += 1
print(count)

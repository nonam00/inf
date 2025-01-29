def check(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True
count = 0
for line in open('6.txt'):
    nums = [int(i) for i in line.split()]
    n3 = [i for i in nums if nums.count(i) == 3]
    n1 = [i for i in nums if nums.count(i) == 1]
    if (len(n3) == 3 and len(n1) == 4) + (nums == sorted(nums)) <= 1:
            count += 1
print(count)

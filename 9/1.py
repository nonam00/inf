count = 0
for line in open('1.txt'):
    nums = [int(i) for i in line.split()]
    if len(nums) == len(set(nums)):
        if len([i for i in nums if i % 2 == 0]) > len([i for i in nums if i % 2 != 0]):
            count += 1
print(count)

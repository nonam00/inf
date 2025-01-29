count = 0
for line in open('10.txt'):
    nums = [int(i) for i in line.split()]
    if ((len(nums) != len(set(nums))) + (len([i for i in nums if i % 2 != 0]) == 3)) == 1:
        count += 1
print(count)

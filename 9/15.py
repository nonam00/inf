count = 0
for line in open('15.txt'):
    nums = [int(i) for i in line.split()]
    n2 = set([i for i in nums if nums.count(i) == 2])
    n1 = [i for i in nums if nums.count(i) == 1]
    if len(n2) == 2 and len(n1) == 3 and sum(n2) / 2 <  sum(nums) / 7:
        count += 1
print(count)

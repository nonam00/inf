count = 0
for line in open('11.txt'):
    nums = [int(i) for i in line.split()]
    mn = min(nums)
    if nums.count(mn) == 1 and len(nums) != len(set(nums)):
        mx = max(nums)
        n2 = [i for i in nums if nums.count(i) > 1]
        if mx + mn < sum(n2):
            count += 1
print(count)
   

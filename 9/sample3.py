for line in open('7.txt'):
    nums = [int(i) for i in line.split()]
    n2 = list(set(i for i in nums if nums.count(i) == 2))
    n1 = [i for i in nums if nums.count(i) == 1]
    if len(n2) == 2 and len(n1) == 2 and max(nums) not in n2:
        mx = max(nums)
        mn = min(nums)
        nums.remove(mx)
        nums.remove(mn)
        if mx * mn > sum(nums):
            print(sum(nums) + mx + mn)
            break
    

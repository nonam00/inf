for line in open('13.txt'):
    nums = [int(i) for i in line.split()]
    n2 = [i for i in nums if nums.count(i) == 2]
    n1 = [i for i in nums if nums.count(i) == 1]
    if len(n2) == 4 and len(n1) == 3 and max(nums) in n1:
        print(sum(nums))
        break

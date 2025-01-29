count = 0
for line in open('2.txt'):
    nums = [int(i) for i in line.split()]
    n4 = [i for i in nums if nums.count(i) == 4]
    n2 = [i for i in nums if nums.count(i) == 2]
    n1 = [i for i in nums if nums.count(i) == 1]
    if len(set(n4)) == 1 and len(set(n2)) == 1 and len(n1) == 3:
        if sum(n1) / 3 >= max(n4[0], n2[0]):
            count += 1
print(count)

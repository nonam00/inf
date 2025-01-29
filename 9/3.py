count = 0 
for line in open('3.txt'):
    nums = [int(i) for i in line.split()]
    povt = list(set([i for i in nums if nums.count(i) == 2]))
    ne = [i for i in nums if nums.count(i) == 1]
    if len(povt) == 2 and len(ne) == 1:
        n = ne[0]
        if (n > povt[0] and n < povt[1]) or (n > povt[1] and n < povt[0]):
            count += 1
print(count)
        


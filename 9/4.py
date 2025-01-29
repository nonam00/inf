for index, line in enumerate(open('4.txt')):
    nums = [int(i) for i in line.split()]
    povt = [i for i in nums if nums.count(i) == 2]
    ne = [i for i in nums if nums.count(i) == 1]
    if len(ne) == 4:
        if povt[0] >= sum(ne) / 4:
            print(index + 1)
            break

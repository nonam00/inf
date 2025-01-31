for i, line in enumerate(open('9.txt')):
    nums = [int(i) for i in line.split()]
    n2 = [i for i in nums if nums.count(i) == 2]
    n1 = [i for i in nums if nums.count(i) == 1]
    if len(n2) == 2 and len(n1) == 4:
        if n2[0] >= sum(n1) / 4:
            print(i + 1)
            break
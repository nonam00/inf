from itertools import permutations
count = 0
for item in list(permutations(range(0, 8), r=5)):
    if item[0] != 0 and item.count(1) == 0:
        count2 = 0
        for i in range(5):
            if (item[i] % 2 == 0 and item[i + 1] % 2 ==0 ) or (item[i] % 2 !=0 and item[i + 1] % 2 !=0):
                count2 += 1
        if count2 == 0:
            count += 1
print(count)
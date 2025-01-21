from itertools import *
count = 0
for item in permutations(range(0,8), r=6):
    if item[0] != 0 and item.count(3) == 0:
        if any(item[i] % 2 == 0 and item[i + 1] % 2 == 0 for i in range(len(item) - 1)):
            count += 1
print(count)
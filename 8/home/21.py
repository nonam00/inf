from itertools import *

count = 0 
for item in product(range(0, 9), repeat=5):
    if item[0] != 0 and item.count(5) == 1:
        count2 = 0
        for i in range(0, 4):
            if item[i] == item[i + 1]:
                count2 += 1
                break
        if count2 == 0:
            count += 1

print(count)
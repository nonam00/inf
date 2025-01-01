from itertools import product
count  = 0
for item in product(range(0, 16), repeat=4):
    if item[0] != 0 and item.count(9) == 1:
        count2 = 0
        for i in range(3):
            if (item[i] % 2 == 0 and item[i + 1] % 2 == 0) or (item[i] % 2 != 0 and item[i + 1] % 2 != 0):
                count2 += 1
        if count2 == 0:
            count += 1

print(count)
from itertools import *
count = 0
for item in product(range(0, 6), repeat=7):
    if item[0] != 0 and item.count(2) == 1:
        ix = item.index(2)
        if ix == 0 and item[ix + 1] % 2 != 0:
            count += 1
        elif ix == 6 and item[ix - 1] % 2 != 0:
            count += 1
        elif item[ix - 1] % 2 != 0 and item[ix + 1] % 2 != 0:
            count += 1
print(count)
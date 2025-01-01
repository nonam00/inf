from itertools import product
count = 0
for item in product(range(0, 7), repeat=6):
    if item[0] != 0 and item[-1] >= 4:
        if len([i for i in item if i % 2 == 0]) == len([i for i in item if i % 2 != 0]):
            count += 1
print(count)
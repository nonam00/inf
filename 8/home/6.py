from itertools import product
count = 0
for item in product('ABCX', repeat=5):
    if item.count('X') == 0 or (item.count('X') == 1 and item[-1] == 'X'):
        count += 1
print(count)
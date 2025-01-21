from itertools import *

letters = sorted(list('ЛОГАРИФМ'))
count = 0
arr = list(product(letters, repeat=5))

for i in range(len(arr)):
    item = ''.join(arr[i])
    if (i + 1) % 2 == 0 and item[0:2] != 'ЛМ' and item.count('И') >= 2:
        count += 1
print(count)
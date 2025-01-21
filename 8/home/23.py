from itertools import *

letters = sorted(list('КОМПЬЮТЕР'))
arr = list(product(letters, repeat=5))

ix = -1
for i in range(len(arr)):
    item = arr[i]
    if item[0] != 'Ь' and item.count('К') == 2:
        ix = i + 1
print(ix)
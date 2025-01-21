from itertools import *
ix1 = -1
letters = sorted(list('НОРМАЛЬЕ'))
arr = [''.join(item) for item in product(letters, repeat=6)]
ix2 = arr.index('НЕНОРМ') + 1
for i in range(len(arr)):
    if arr[i][0:4] == 'НОРМ':
        ix1 = i + 1
        break
print(ix2 - ix1)
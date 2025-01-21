from itertools import *
letters = sorted(list('АКЛМНЯ'))
ix1 = -1
ix2 = -1
arr = list(product(letters, repeat=5))
for i in range(len(arr)):
    if arr[i][0] == 'М' and arr[i][1] == 'Н':
        if ix1 == -1: ix1 = i + 1
        ix2 = i + 1
print(ix2 - ix1 - 1)
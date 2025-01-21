from itertools import *
ix = -1
letters = sorted(list('МАНГУСТ'))
arr = list(product(letters, repeat=6))
for i in range(len(arr)):
    item = arr[i]
    if item[0] != 'У' and item.count('М') == 2 and item.count('Г') <= 1:
        ix = i + 1
print(ix)
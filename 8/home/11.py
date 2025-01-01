from itertools import product
letters = sorted(list('МАНГУСТ'))
ix = 0
arr = list(product(letters, repeat=6))
for i in range(len(arr)):
    if arr[i][0] != 'У' and arr[i].count('М') == 2 and arr[i].count('Г') <= 1:
        ix = i
print(ix + 1)
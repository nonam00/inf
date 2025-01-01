from itertools import product
ix = 0
letters = sorted(list('ГИРЛЯНДА'))
arr = list(product(letters, repeat=6))
for i in range(len(arr)):
    if ((i + 1) % 2 == 0) and arr[i][0] != 'Я' and arr[i].count('Д') == 3:
        ix = i
print(ix + 1)
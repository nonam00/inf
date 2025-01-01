from itertools import product
letters = sorted(list('ГОНДУБШ'))
arr = list(product(letters, repeat=6))
ix = 0
for i in range(len(arr)):
    if ((i + 1) % 2 != 0) and arr[i][0] != 'Б' and arr[i].count('Н') >= 2 and arr[i].count('У') == 0:
        ix = i + 1
print(ix)
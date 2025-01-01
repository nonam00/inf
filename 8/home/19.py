from itertools import product
letters = sorted(list('КОМПЬЮТЕР'))
arr = list(product(letters, repeat=5))
ix = -1
for i in range(len(arr)):
    if (i + 1) % 2 != 0 and arr[i][0] != 'Ь' and arr[i].count('К') == 2:
        ix = i + 1
print(ix)
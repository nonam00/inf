from itertools import product
ix = -1
letters = sorted(list('БМЮРН'))
arr = list(product(letters, repeat=6))
for i in range(len(arr)):
    if (i + 1) % 2 != 0 and arr[i][0] != 'М' and arr[i].count('Р') >= 2 and arr[i].count('Ю') == 0:
        ix = i + 1
print(ix)
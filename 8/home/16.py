from itertools import product
letters = sorted(list('ЛЕМУР'))
arr = list(product(letters, repeat=4))
for i in range(len(arr)):
    if arr[i][0] == 'Л':
        print(i + 1)
        break
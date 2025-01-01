from itertools import product
letters = sorted(list('АКЛМНЯ'))
arr = list(product(letters, repeat=5))
index1 = -1
index2 = -1
for i in range(len(arr)):
    if arr[i][0] + arr[i][1] == 'МН':
        if index1 == -1:
            index1 = i + 1
        index2 = i + 1
print(index2 - index1 -1 )
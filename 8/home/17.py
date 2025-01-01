from itertools import product
letters = sorted(list('НОРМАЛЬЕ'))
index1 = -1
arr = [''.join(item) for item in (product(letters, repeat=6))]
for i in range(len(arr)):
    item = arr[i]
    if item[:4] == 'НОРМ':
        index1 = i + 1
        break
index2 = arr.index('НЕНОРМ') + 1
count = index2 - index1
print(count)
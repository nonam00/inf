from  itertools import product
letters = sorted(list('АПРЕЛЬ'))[::-1]
arr = list(product(letters, repeat=5))
count = 0
for i in range(387):
    if arr[i][-1] == 'Ь':
        count += 1
print(count)
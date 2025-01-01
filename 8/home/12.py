from itertools import product
letters = sorted(list('ЛОГАРИФМ'))
arr = list(product(letters, repeat=5))
count = 0
for i in range(len(arr)):
    item = arr[i]
    if ((i+1) % 2 == 0) and (item[0] + item[1] != 'ЛМ') and item.count('И') >= 2:
        count += 1
print(count)
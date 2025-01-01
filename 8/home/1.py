from itertools import permutations
arr = list('0246')
count = 0
for item in list(permutations('0124567', r=6)):
    if item[0] == '0':
        continue
    count2 = 0
    for i in range(5):
        if int(item[i]) % 2 == 0 and int(item[i+1]) % 2 == 0:
            count2 += 1
    if count2 != 0:
        count += 1
print(count)
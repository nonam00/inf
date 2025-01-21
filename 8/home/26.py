from itertools import *
count = 0
bad1 = list(product('АИЯ', repeat=3))
bad2 = list(product('НСТ', repeat=3))
for item in set(permutations(('АНАСТАСИЯ'), r=9)):
    s = ''.join(item)
    if all(not (''.join(i) in s and ''.join(j) in s) for i in bad1 for j in bad2):
        count += 1
print(count)

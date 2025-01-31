from itertools import *
letters = sorted(list('БМЮРН'))
p = list(product(letters, repeat=6))
x = -1
for i in range(len(p)):
    s = p[i]
    if s[0] != 'М' and s.count('Р') >= 2 and s.count('Ю') == 0:
        x = i + 1
print(x)
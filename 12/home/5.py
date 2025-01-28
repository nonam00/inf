def f(s):
    while '12' in s or '233' in s or '3333' in s:
        s = s.replace('12', '332', 1)
        s = s.replace('233', '23', 1)
        s = s.replace('3333', '32', 1)
    return sum(map(int, s))

for n in range(6, 100):
    if f('1' + ('3' * n)) % 6 == 0:
        print(n)

def f(s):
    while '25' in s or '35' in s or '555' in s:
        s = s.replace('25', '53', 1)
        s = s.replace('35', '2', 1)
        s = s.replace('555', '23', 1)
    return sum(map(int, s))

for n in range(4, 100):
    if f('2' + ('5' * n)) % 7 == 0:
        print(n)

def f(s):
    while '25' in s or '355' in s or '555' in s:
        s = s.replace('25', '32', 1)
        s = s.replace('355', '25', 1)
        s = s.replace('555', '3', 1)
    return sum(map(int, s))

for n in range(11, 1000):
    val = f('3' + n * '5')
    if val % 25 == 0:
        print(n)


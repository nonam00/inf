def f(s):
    while '52' in s or '2222' in s or '1122' in s:
        s = s.replace('52', '11')
        s = s.replace('2222', '5')
        s = s.replace('1122', '25')
    return sum(map(int, s))

for n in range(3, 10_000):
    if f('5' + ('2' * n)) == 64:
        print(n)

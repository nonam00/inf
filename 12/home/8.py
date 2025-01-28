def f(s):
    while '31' in s or '32' in s or '30' in s:
        s = s.replace('31', '223', 1)
        s = s.replace('32', '23', 1)
        s = s.replace('30', '13', 1)
    s = s.replace('3', '0', 1)
    return sum(map(int, s))

for n in range(1, 100):
    val = str(f('3' + (40 * '0') + (n * '1') + (40 * '2')))
    if len(val) == 3 and len(set(val)) == 1:
        print(n)

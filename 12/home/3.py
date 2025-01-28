def f(s):
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1', '22>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>0', '1>', 1)
    return s

for n in range(1, 1000):
    val = f('>' + (40 * '0') + (n * '1') + (40 * '2'))
    sm = str(sum([int(x) for x in val if x != '>']))
    if sm[0] != '0' and len(sm) == 3 and len(set(sm)) == 1:
        print(n)

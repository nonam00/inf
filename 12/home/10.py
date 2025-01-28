def f(s):
    while '23' in s or '5333' in s or '33333' in s:
        s = s.replace('23', '3', 1)
        s = s.replace('5333', '32', 1)
        s = s.replace('33333', '55', 1)
    return sum(map(int, s))

mn = float('inf')
for n in range(4, 2000):
    val = f(n * '3' + '5')
    if val < mn:
        print(val)
        mn = val

def f(s):
    while '46' in s or '666' in s:
        s = s.replace('46', '5', 1)
        s = s.replace('666', '4', 1)
    return sum(map(int, s))

for n in range(1, 1000):
    val = f('4' + n * '6')
    if val > 1000:
        print(n)

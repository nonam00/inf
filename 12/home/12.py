def f(s):
    while '15' in s or '255' in s or '555' in s:
        s = s.replace('15', '2', 1)
        s = s.replace('255', '1', 1)
        s = s.replace('555', '12', 1)
    return sum(map(int, s))

for n in range(6, 10000):
    val = f('1' + n * '5' + '2' + n * '5')
    if len(str(val)) == 3:
        print(n)

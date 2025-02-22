def f(s):
    while '31' in s or '32' in s or '30' in s:
        s = s.replace('31', '223')
        s = s.replace('32', '23')
        s = s.replace('30', '13')
    return s.replace('3', '0')

for n in range(0, 1000):
    s = f'3{40 * '0'}{n * '1'}{40 * '2'}'
    val = f(s)
    sm = str(sum(map(int, val)))
    if len(sm) == 3 and len(set(sm)) == 1:
        print(n)
        break
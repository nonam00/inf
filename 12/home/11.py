def f(s):
    while '13' in s or '31' in s or '11' in s:
        s = s.replace('13', '4', 1)
        s = s.replace('31', '1', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('44', '1', 1)

    return sum(map(int, s))

mx = -float('inf')
for n in range(1, 100):
    val = f(n * '13')
    if len(str(val)) == 2 and val > mx:
        print(val, n)
        mx = val

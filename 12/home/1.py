def f(s):
    while s.count('555') > 0 or s.count('11') > 0 or s.count('2'):
        s = s.replace('555', '1', 1)
        s = s.replace('11', '25', 1)
        s = s.replace('2', '5', 1)
    return int(s)

mx_val = -float('inf')
for n in range(101, 200):
    if n % 9 == 0:
        val = f('5' * n)
        if val > mx_val:
            mx_value = val
            print(val, n)

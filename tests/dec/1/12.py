def f(s):
    while '555' in s or '11.py' in s or '2' in 's':
        s = s.replace('555', '1', 1)
        s = s.replace('11.py', '25', 1)
        s = s.replace('2', '5', 1)
    return int(s)

mx_value = -float('inf')

for n in range(101, 10000):
    if n % 9 == 0:
        val = f('5' * n)
        if val > mx_value:
            mx_value = val
            print(val, n)
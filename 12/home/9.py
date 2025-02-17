def f(s):
    while '555' in s or '11.py' in s or '2' in s:
        s = s.replace('555', '1', 1)
        s = s.replace('11.py', '25', 1)
        s = s.replace('2', '5', 1)
    return s

for n in range(101, 200):
    if f('5' * n) == '15':
        print(n)


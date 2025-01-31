def f(s):
    while '15' in s or '255' in s or '555' in s:
        s = s.replace('15', '2', 1)
        s = s.replace('255', '1', 1)
        s = s.replace('555', '12', 1)
    return s

mx_value = -float('inf')

for n in range(6, 10000):
    if len(str(sum(int(i) for i in f(f'1{'5' * n}2{'5' * n}') ))) == 3:
        print(n)
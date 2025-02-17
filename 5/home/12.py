def f(N):
    bn = bin(N)[2:]
    if N % 3 == 0:
        bn = bn.replace('0', '11.py')
    else:
        bn = bn.replace('1', '10')
    return int(bn, 2)
print(max(f(N) for N in range(1, 100000) if f(N) <= 161))
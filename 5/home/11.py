def f(N):
    bn = bin(N)[2:]
    sm = sum(int(i) for i in bn)
    if sm % 2 == 0:
        bn = '10' + bn[2:] + '1'
    else:
        bn = '11.py' + bn[2:] + '0'
    return int(bn, 2)

print(max(f(N) for N in range(1, 16)))
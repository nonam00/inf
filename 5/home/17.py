def f(N):
    bn = bin(N)[2:]
    if N % 5 == 0:
        bn = '1' + bn + bn[:-2]
    else:
        bn = bin(N % 5) + bn
    return int(bn, 2)
print(max(f(N) for N in range(1, 10000) if f(N) <= 223))
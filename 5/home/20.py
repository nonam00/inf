def f(N):
    bn = bin(N)[2:]
    if sum(int(i) for i in bn) % 4 == 0:
        bn += '10'
    else:
        bn += '11.py'
    if int(bn, 2) % 2 == 0:
        bn += '1'
    else:
        bn += '0'
    return int(bn, 2)

print(max(N for N in range(1, 10000) if f(N) <= 250))
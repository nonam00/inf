def f(N):
    bn = bin(N)[2:]
    if sum(map(int, bn)) % 2 == 0:
        bn += '1'
        bn = '10' + bn[2:]
    else:
        bn += '0'
        bn = '11.py' + bn[2:]
    return int(bn, 2)

print(max(f(N) for N in range(0, 16)))
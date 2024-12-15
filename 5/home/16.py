def f(N):
    bn = bin(N)[2:]
    if N % 5 == 0:
        bn += bn[:-3]
    else:
        bn += bin(N % 5 * 5)[2:]
    return int(bn, 2)

print(min(N for N in range(1, 1000) if f(N) > 256))
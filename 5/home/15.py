def f(N):
    bn = bin(N)[2:]
    bn += str(sum(int(i) for i in bn) % 2)
    bn += str(sum(int(i) for i in bn) % 2)
    return int(bn, 2)

print(min(N for N in range(1, 1000) if f(N) > 77))
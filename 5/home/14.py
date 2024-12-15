def f(N):
    bn = bin(N)[2:]
    bn += str(sum(int(i) for i in bn) % 2)
    bn += str(sum(int(i) for i in bn) % 2)
    return int(bn, 2)

print(min(f(N) for N in range(1, 100000) if f(N) > 80))
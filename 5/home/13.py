def f(N):
    bn = bin(N)[2:]
    bn += bin(N % 4)[2:]
    return int(bn, 2)

dost = [f(N) for N in range(1, 10000)]
mx = -float('inf')
print(max(len([x for x in dost if i <= x <= i + 64]) for i in range(1, 10000)))
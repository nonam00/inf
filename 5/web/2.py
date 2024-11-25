def f(N):
    b = bin(N)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    return int(b, 2)

print(min([N for N in range(1, 2000) if f(N) > 77]))

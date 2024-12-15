def f(N):
    x = oct(N)[2:]
    if N % 7 == 0:
        x += x[-2:]
    else:
        x += oct(N % 7 * 7)[2:]
    return int(x, 8)

print(len(set(f(N) for N in range(1, 10000) if f(N) < 3000)))
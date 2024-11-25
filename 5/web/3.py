def f(N):
    b = bin(N)[2:]
    if N % 2 == 0:
        b = '10' + b
    if N % 2 != 0:
        b = '1' + b + '01'
    return int(b, 2)

print(max([f(N) for N in range(1, 13)]))


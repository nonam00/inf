def c(x):
    b = ''
    while x > 0:
        b = str(x % 3) + b
        x //= 3
    return b

def f(N):
    b = c(N)
    if N % 3 == 0:
        b = '1' + b + '02'
    else:
        b += c(N % 3 * 4)
    return int(b, 3)

print(max(N for N in range(1, 10000) if f(N) < 199))

def dels(n, m):
    return n % m == 0

def f(A, x):
    return (dels(x, 3) <= (not dels(x, 2) )) or (x - A >= 4)

print(max(A for A in range(1, 500) if all(f(A, x) for x in range(1, 500) )))
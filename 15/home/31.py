B = range(40, 61)
def d(n, m): return n % m == 0
def f(x, A):
    return (d(x, 13) <= (x not in B)) or (A < x + 20)
print(max(A for A in range(1, 500) if all(f(x, A) for x in range(1, 200))))

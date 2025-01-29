def d(n, m): return n % m == 0
def f(x, A):
    return (d(x, 2) <= (not d(x, 3))) or (x + A >= 100)
print(min(A for A in range(1, 500) if all(f(x, A) for x in range(1, 500))))

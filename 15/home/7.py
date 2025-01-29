def d(x, d): return x % d == 0
def f(x, A): return (d(x, 10) and d(x, 26) and (x >= 300)) <= (A <= x)
print(max(A for A in range(1, 500) if all(f(x, A) for x in range(1, 500))))

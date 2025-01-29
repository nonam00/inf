def d(n, m): return n % m == 0
def s(s, d): return s + d > 0
def f(x, A):
    return (x + A >= 160) or (d(x, 7) <= (not s(x, -17)))
print(min(A for A in range(1, 500) if all(f(x, A) for x in range(1, 500))))

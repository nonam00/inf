def DEL(n, m):
    return n % m == 0
def SUM(s, d):
    return (s + d) > 0
def f(x, A):
    return (x + A >= 160) or DEL(x, 7) <= (not(SUM(x, -17)))

print(min(A for A in range(1, 400) if all(f(x, A) == 1 for x in range(1, 500))))

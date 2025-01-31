def f(a, m):
    if a >= 55: return m % 2 == 0
    if m == 0: return 0

    d = [f(a + 1, m - 1), f(a + 4, m - 1), f(a * 3, m - 1)]

    return any(d) if m % 2 != 0 else all(d)

print([s for s in range(1, 54) if f(s, 2)])
print([s for s in range(1, 54) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 54) if not f(s, 2) and f(s, 4)])

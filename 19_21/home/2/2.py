def f(s, m, prev=''):
    if s > 40: return m % 2 == 0
    if m == 0: return 0
    h = []
    if prev != '+3':
        h.append(f(s + 3, m - 1, '+3'))
    if prev != '+6':
        h.append(f(s + 6, m - 1, '+6'))
    if prev != '*2':
        h.append(f(s * 2, m - 1, '*2'))
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(2, 37) if f(s, 2)])
print([s for s in range(2, 37) if not f(s, 1) and f(s, 3)])
print([s for s in range(2, 37) if not f(s, 2) and f(s, 4)])



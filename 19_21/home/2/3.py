def f(s, m, prev='', prev2=''):
    if s >= 29: return m % 2 == 0
    if m == 0: return 0
    h = []
    if prev2 != '+1':
        h.append(f(s + 1, m - 1, '+1', prev))
    if prev2 != '+2':
        h.append(f(s + 2, m - 1, '+2', prev))
    if prev2 != '*2':
        h.append(f(s * 2, m - 1, '*2', prev))
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(1, 29) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 29) if not f(s, 2) and f(s, 4)])
print([s for s in range(1, 29) if not f(s, 1) and (not f (s, 3)) and f(s, 5)])
    

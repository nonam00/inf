def f(n, end, prev='', prev2=''):
    if n > end: return 0
    if n == end: return 1
    if prev == '+1' and prev2 == '+1':
        return f(n * 2, end, '*2', prev)
    if prev == '*2' and prev2 == '*2':
        return f(n + 1, end, '+1', prev)
    return f(n + 1, end, '+1', prev) + f(n * 2, end, '*2', prev)
print(f(1, 16))
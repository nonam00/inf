def f(x, end):
    if x < end: return 0
    if x == end: return 1
    return f(x - 3, end) + f(x // 2, end) + f(x - 5, end)
print(f(43, 32) * f(32, 16))

def f(x, end):
    if x == end: return 1
    if x > end: return 0
    return f(x + 4, end) + f(x * 2, end)
print(f(13, 42))

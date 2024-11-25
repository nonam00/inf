def f(x, end):
    if x > end: return 0
    if x == end: return 1
    if x == 32: return 0
    return f(x + 2, end) + f(x + 4, end)
print(f(9,27) * f(27, 29) * f(29, 37))

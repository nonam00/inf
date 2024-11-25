def f(x, end):
    if x == end: return 1
    if x > end: return 0
    return f(x + 2, end) + f(x + 3, end) + f(int(str(x) + '1'), end)
print(f(3, 12) * f(12, 25))

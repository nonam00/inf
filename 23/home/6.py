def f(x, end):
    if x > end: return 0
    if x == end: return 1
    if x == 13: return 0
    return f(x+1, end) + f(x+2, end) + f(x*3, end)
print(f(3, 8) * f(8, 18))

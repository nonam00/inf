def f(x, end):
    if x > end: return 0
    #if x == 32: return 0
    if x == 16: return 0
    if x == end: return 1
    return f(x + 3, end) + f(x + 5, end) + f(x * 2, end)

print(f(4, 16) * f(16, 68)) 

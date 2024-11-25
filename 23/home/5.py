def f(x, end, skip):
    if x == end: return 1
    if x > end: return 0  
    if x == skip: return 0
    return f(x + 1, end, skip) + f(x + 2, end, skip) + f(x * 3, end, skip)

print(f(6, 15, 21) * f(15, 25, 21) + f(6, 21, 15) * f(21, 25, 15))

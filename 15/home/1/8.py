def f(x, y, A):
    return (x >= 9) or ((2*x) < y) or ((x*y) < A)
print(min(A for A in range(0, 200) if all(f(x,y,A) for x in range(0, 200) for y in range(0, 200))))

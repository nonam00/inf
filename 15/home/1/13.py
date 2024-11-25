def pos(n, m):
    return n - m >= 0
def f(x, y, A):
    return (not(pos(x+y, 73))) or (not(pos(37, x-y))) or pos(y,A)
print(max(A for A in range(0, 400) if all(f(x,y,A) for x in range(0,400) for y in range(0,400))))


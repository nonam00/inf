def f(x, A):
    return (x & A != 0) <= (((x & 17 == 0) and (x & 5 == 0)) <= (x & 3 != 0)) 
print(max(A for A in range(0, 500) if all(f(x, A) for x in range(0, 500))))

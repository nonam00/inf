def f(x, A):
    return ((x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & A != 0) and (x & 58 ==0))
print(min(A for A in range(1, 200) if all(f(x,A) == False for x in range(1, 200))))

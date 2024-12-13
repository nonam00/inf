def f(N):
    bn = bin(N)[2:]
    if N % 5 == 0: bn += bin(5)[2:]
    else: bn += '1'
    
    if int(bn, 2) % 7 == 0:
        bn += bin(7)[2:]
    else:
        bn += '1'
    return int(bn, 2)

print(max(N for N in range(1,1000000) if f(N) < 1_855_663))

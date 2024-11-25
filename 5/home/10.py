def f(N):
    b = bin(N)[2:]
    if N % 5 == 0:
        b += bin(5)[2:]
    else:
        b += '1'
    
    if int(b, 2) % 7 == 0:
        b += bin(7)[2:]
    else:
        b += '1'

    return int(b, 2)

print(max(N for N in range(0, 10000000) if f(N) < 1855663))

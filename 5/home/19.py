def f(n):
    x = ''
    while n > 0:
        x = str(n % 5) + x
        n //= 5
    if int(x[-1], 5) % 2 == 0:
        x += '2'
    else:
        x = '2' + x + '3'
    return int(x, 5) 

print(max(N for N in range(1, 10000) if f(N) < 1000))
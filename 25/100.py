def p(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
def d(n):
    arr = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and i != n // i and p(i) and (n // i):
            arr.append(i)
            arr.append(n // i)
    return arr

r = float('inf')
for i in range(523456, 578925 + 1):
    dels = d(i)
    if len(dels) == 2:
        tmp = abs(dels[0] - dels[1])
        if tmp <= r:
            print(i, sorted(dels))
            r = tmp


A = 0
for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = 254 <= x <= 800
    Q = 410 <= x <= 823
    f = ((P) and (not(A))) <= (Q)
    if f != 1:
        print(x)

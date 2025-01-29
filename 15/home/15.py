A = 0
for x in [0.25 * i for i in range(-10000, 10000)]:
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    f = D <= (((not C) and (not A)) <= (not D))
    if f != 1:
        print(x)

A = 0
for x in [i * 0.25 for i in range(-10000, 10000)]:
    D = 17 <= x <= 58
    C = 29 <= x <= 80
    f = D <= (((not C) and (not A)) <= (not D))
    if f != 1:
        print(x)

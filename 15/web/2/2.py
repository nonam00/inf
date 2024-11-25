f_usl = 1
A = 1 # т.к наибольшее
for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = 3 <= x <= 15
    Q = 14 <= x <= 25
    f = (P == Q) <= (not A)
    if f == f_usl:
        print(x)

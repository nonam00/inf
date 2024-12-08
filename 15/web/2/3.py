f_usl = 1
A = 0
for x in [k * 0.25 for k in range(-10000, 10000)]:
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    f = (not(M or N)) == (not A)
    if f != f_usl:
        print(x)


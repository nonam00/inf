A = 1
for x in [0.25 * i for i in range(-10000, 10000)]:
    P = 44 <= x <= 49
    Q = 28 <= x <= 53
    f = (A <= P) or Q
    if f == 1:
        print(x)

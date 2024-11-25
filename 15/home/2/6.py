A = 0
for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = 25 <= x <= 240
    Q = 175 <= x <= 300
    R = 270 <= x <= 340
    f = ((Q) <= (P)) or ((not(A)) <= (R))
    if f != 1:
        print(x)

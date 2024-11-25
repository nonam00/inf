A = 0
for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = 5 <= x <= 280
    Q = 295 <= x <= 400
    R = 375 <= x <= 450
    f = ((Q) <= (P)) or ((not(A)) <= (R))
    if f != 1:
        print(x)

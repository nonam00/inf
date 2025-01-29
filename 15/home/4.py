A = 0
for x in [i * 0.25 for i in range(-10000, 10000)]:
    P = 12 <= x <= 28
    Q = 15 <= x <= 30
    f = (P <= A) and ((not Q) or (A))
    if f != 1:
        print(x)

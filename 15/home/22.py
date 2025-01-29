A = 0
for x in [0.25 * i for i in range(-10000, 10000)]:
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    f = (B <= A) and ((not C) or A)
    if f != 1:
        print(x)

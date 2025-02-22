A = 0
for x in [0.25 * i for i in range(-10000, 10000)]:
    P = 35 <= x <= 55
    Q = 45 <= x <= 65
    f = (P <= A) and ((not A) <= (not Q)) 
    if f != 1:
        print(x)

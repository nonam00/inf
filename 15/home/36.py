P = [1, 3, 4, 9, 11, 13, 15, 17, 19, 21]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
A = 0
for x in [0.25 * i for i in range(-10000, 10000)]:
    f = ((x in P) <= (A)) or ((not A) <= (x not in Q))
    if f != 1:
        print(x)

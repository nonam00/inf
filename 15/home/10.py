P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
A = 1
for x in [i * 0.25 for i in range(-10000, 10000)]:
    f = ((A) <= (x in P)) and ((not (x in Q)) <= (not A))
    if f == 1:
        print(x)

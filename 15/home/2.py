P = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
Q = set([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

A = 1
for x in [i * 0.25 for i in range(-10000, 10000)]:
    f = (A <= (x in P)) and ((x in Q) <= (not A))
    if f == 1:
        print(x, end=" ")

A = 0
P = [1, 3, 4, 9, 11, 13, 15, 17, 19, 21]
Q = [i for i in range(3, 31) if i % 3 == 0]
res = 1
for x in [k * 0.25 for k in range(-10000, 10000)]:
    f = ((x in P) <= (A)) or ( (not(A)) <= (not(x in Q)) )
    if f != 1:
        print(x)
        res *= x
print(res)

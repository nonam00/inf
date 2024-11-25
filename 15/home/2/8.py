P = [i for i in range(2, 21) if i % 2 == 0]
Q = [i for i in range(3, 31) if i % 3 == 0]
A = 1
for x in [i * 0.25 for i in range(-10000, 10000)]:
    f = ((A) <= (x in P)) and ((not(x in Q)) <= (not(A)))
    if f == 1:
         print(x)

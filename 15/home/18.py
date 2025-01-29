A = 1
a = [12, 23, 34, 45, 56]
b = [23, 35, 56, 68, 89]
for x in [0.25 * i for i in range(-10000, 10000)]:
    f = (x in a) or (x in b) or (not A)
    if f == 1:
        print(x)

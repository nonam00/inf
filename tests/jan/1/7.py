Id = 25 * 1024 * 1024 * 8
n = 2
f = 50 * 1000
i = 16
dop = 40 * 1024 * 8

Id2 = Id - dop
I = Id2 * 100 / 75
t = I / f / i / n
print(t / 60)

def f(n):
    if n == 0: return 0
    if n > 0 and n % 2 == 0: return f(n / 2) - 1
    if n > 0 and n % 2 != 0: return 1 + f(n - 1)

count = 0
for i in range(0, 1000):
    if f(i) == 0:
        count += 1
print(count)
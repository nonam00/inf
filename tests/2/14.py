x = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25** 4 - 2024
count = 0
y = ''
while x > 0:
    y = str(x % 25) + y
    x //= 25
while y[0] == '0': y = y[1:]
print(y.count('0'))
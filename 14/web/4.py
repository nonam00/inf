mx = -float('inf')
for x in range(1, 2031):
    y = 7 ** 170 + 7 ** 100 - x
    count = 0
    while y > 0:
        if y % 7 == 0:
            count += 1
        y //=7
    if count == 71:
        print(x)

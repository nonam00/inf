#18616
for x in range(0, 37):
    x1 = sum(c * 37 ** i for i, c in enumerate([int('C', 36), 5, 9, x, int('A', 36), int('A', 36), 9, 8, int('F', 36)][::-1]))
    x2 = sum(c * 37 ** i for i, c in enumerate([int('E', 36), 3, x, 5, int('D', 36), int('A', 36), 9, int('C', 36), 6][::-1]))
    if (x1 * x2) % 36 == 0:
        x3 = sum(c * 37 ** i for i, c in enumerate([2, x, 1][::-1]))
        print(x, x3)

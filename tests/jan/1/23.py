def f(a, end, flag1 = False, flag2 = False):
    if a == 15: flag1 = True
    if a == 21: flag2 = True
    if flag1 and flag2: return 0
    if a > end: return 0
    if a == end:
        if flag1 or flag2: return 1
        else: return 0
    return f(a + 1, end, flag1, flag2) + f(a + 2, end, flag1, flag2) + f(a * 3, end, flag1, flag2)

print(f(6, 25))
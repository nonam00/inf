for x in '0123456789ABCDEFGHIJKLMNOPQRS':
    v1 = int(f'47{x}42696', 29)
    v2 = int(f'8{x}22', 29)
    if (v1 + v2) % 28 == 0:
        print(x)
        print((v1 + v2) / 28)


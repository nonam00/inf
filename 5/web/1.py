for N in range(1, 200):
    b = bin(N)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    R = int(b, 2)
    if R > 77:
        print(N)
        break

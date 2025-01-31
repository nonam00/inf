dic = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
}
arr = set()
for x in '0123456789ABCDEFGH':
    for y in range(9, 18):
        if int(x, 18) >= y: continue
        yt = str(y)
        if y >= 10:
            yt = dic[y]
        res = int(f'5{x}{yt}A', 18) + int(f'18{x}7', y)
        arr.add(res)
print(len(arr))
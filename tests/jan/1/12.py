def f(s):
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1', '22>')
        s = s.replace('>2', '2>')
        s = s.replace('>0', '1>')
    return s.replace('>', '')
for n in range(1, 1000):
    s = f'>{'0'*40}{'1'*n}{'2'*40}'
    val = str(sum(map(int, f(s))))
    if val[0] != '0' and len(val) == 3 and len(set(val)) == 1:
        print(n)
        break
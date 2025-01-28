def f(s):
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    return len(s)

mx = -float('inf')
for n in range(4, 1000):
    val = f('1' + n * '2')
    if val > mx:
        mx = val
        print(val)

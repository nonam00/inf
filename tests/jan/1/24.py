s = open('24.txt').readline()
mx = -float('inf')
t = ''
for i in range(len(s)):
    t += s[i]
    if t.count('X') > 1 or t.count('Y') > 1: t = t[1:]
    mx = max(mx, len(t))
print(mx)
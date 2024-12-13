s = open('24.txt').readline()
while 'AB' in s: s = s.replace('AB', 'A B')
mx = -float('inf')
s = s.split(' ')
for i in range(len(s) - 50):
    sm = sum(len(item) for item in s[i:i+51])
    mx = max(mx, sm)
print(mx)


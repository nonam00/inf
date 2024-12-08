s = open('3.txt').readline()
while 'AB' in s: s = s.replace('AB', 'A B')
s = s.split(' ')
mx = -float('inf')
for i in range(len(s) - 50):
    sm = sum(len(item) for item in s[i:i+51])
    mx = max(mx, sm)
print(mx)
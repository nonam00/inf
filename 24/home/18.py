a = open('18.txt').readline()
mx = -float('inf')
s = ''
for i in range(len(a)):
    s += a[i]
    if s[-3:] == 'ROR': s = 'OR'
    if s[-3:] == 'ORO': s = 'RO'
    while s.count('RO') > 21: s = s[1:]
    if s.count('RO') == 21: mx = max(mx, len(s))
print(mx)
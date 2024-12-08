s = open('6.txt').readline()
while 'XX' in s: s = s.replace('XX', '1')
while 'YY' in s: s = s.replace('YY', '2')
while 'ZZ' in s: s = s.replace('ZZ', '3')

m = -float('inf')
for i in range(len(s) - 1):
    if s[i] in '123' and s[i + 1] in '123' and s[i] != s[i + 1]:
        count += 1
        m = max(m, count)
    else:
        count = 1
print(m * 2)

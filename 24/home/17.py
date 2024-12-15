s = open('17.txt').readline()
while 'NPO' in s: s = s.replace('NPO', '***')
while 'PNO' in s: s = s.replace('PNO', '***')
mx = -float('inf')
count = 0
for i in range(len(s)):
    if s[i] == '*':
        count += 1
        mx = max(mx, count)
    else:
        count = 0
print(mx)
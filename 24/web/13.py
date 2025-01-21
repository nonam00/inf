s = open('24_8615.txt').readline()

for c in 'ABCDEF': s = s.replace(c, 'Я')

ps = ''
mps = ''
for i in range(len(s)):
    ps += s[i]
    if ps[-3:] == 'ЯЯЯ':
        ps = 'ЯЯ'
    if len(ps) > len(mps):
        mps = ps 

print(len(mps))
s = open('4.txt').readline()
while 'NPO' in s: s = s.replace('NPO', '*')
while 'PNO' in s: s = s.replace('PNO', '*')
for c in 'NPO': s = s.replace(c, ' ')
print(max(len(kusok) for kusok in s.split(' ')))

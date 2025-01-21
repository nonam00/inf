s = open('24_9075.txt').readline()
for c in '0468': s = s.replace(c, '2')
for c in '3579': s = s.replace(c, '1')

while '12' in s: s = s.replace('12', '1 2')
while '21' in s: s = s.replace('21', '2 1')

s = s.split()
print(max(len(kusok) for kusok in s))
s = open('22.txt').readline()
s = s.replace('-', '*')
s = s.replace('7', '1')
s = s.replace('8', '1')
s = s.replace('9', '1')
while '**' in s: s = s.replace('**', '* *')
mx = -float('inf')
for item in s.split():
    if len(item) < mx:
        continue
    for i in range(len(item) - 1):
        ps = item[i]
        if item[i] != '*' and item[i] + item[i + 1] not in ['00','01']:
            for j in range(i + 1, len(item)):
                ps += item[j]
                if ps[-1] != '*' and all(z[0] != '0' for z in ps.split('*')):
                    mx = max(len(ps), mx)
print(mx)
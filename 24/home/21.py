s = open('21.txt').readline()
for i in range(2, 10):
    s = s.replace(str(i), '1')
while '**' in s: s = s.replace('**', '* *')
while '++' in s: s = s.replace('++', '+ +')
while '*+' in s: s = s.replace('*+', '* +')
while '+*' in s: s = s.replace('+*', '+ *')
symbols = '+*'
mx = -float('inf')
bad = ['0' + str(i) for i in range(0, 10)]
for item in s.split(' '):
    if len(item) < mx:
        continue
    for i in range(len(item) - 1):
        ps = item[i]
        if item[i] not in symbols and item[i] + item[i + 1] not in bad:
            for j in range(i + 1, len(item)):
                ps += item[j]
                if ps[-1] not in symbols:
                    if eval(ps) == 0:
                        mx = max(len(ps), mx)
print(mx)
s = open('5.txt').readline()
while '++' in s: s = s.replace('++', '+ +')
while '**' in s: s = s.replace('**', '* *')
while '+*' in s: s = s.replace('+*', '+ *')
while '*+' in s: s = s.replace('*+', '* +')
symbols = '+*'
mx = -float('inf')
for item in s.split():
    if len(item) < mx:
        continue
    for i in range(len(item) - 1):
        ps = item[i]
        if item[i] not in symbols and item[i] + item[i + 1] not in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']:
            for j in range(i + 1, len(item)):
                ps += item[j]
                if ps[-1] not in symbols:
                    if eval(ps) == 0:
                        mx = max(len(ps), mx)
print(mx)
s = open('8.txt').readline()
symbols = '-*'
while '--' in s: s = s.replace('--', '- -')
while '**' in s: s = s.replace('**', '* *')
while '*-' in s: s = s.replace('*-', '* -')
while '-*' in s: s = s.replace('-*', '- *')
mx = -float('inf')
for item in s.split():
    if mx < len(item):
        for i in range(len(item) - 1):
            ps = item[i]
            if ps[0] == 'B': 
                for j in range(i + 1, len(item)):
                    ps += item[j]
                    if ps[1] not in '-*' and ps[-1] not in '-*':
                        if 'A' not in ps and 'C' not in ps and 'D' not in ps:
                            if ps.count('B') == 1:
                                mx = max(mx, len(ps))
print(mx)
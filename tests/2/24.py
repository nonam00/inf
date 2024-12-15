s = open('24.txt').readline().replace('-', '*')
while '**' in s: s = s.replace('**', '* *')
mx = -float('inf')
for item in s.split():
    if len(item) < mx:
        continue
    for i in range(len(item) - 1):
        ps = item[i]
        if item[i] != '*' and item[i] != '0':
            for j in range(i + 1, len(item)):
                ps += item[j]
                if ps[-1] != '*' and any(x[0] == '0' for x in ps.split('*')):
                    continue
                if ps[-1] != '*':
                    mx = max(len(ps), mx)
print(mx)
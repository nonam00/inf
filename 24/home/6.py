s = open('6.txt').readline()
symbols = '-*'
while '--' in s: s = s.replace('--', '- -')
while '**' in s: s = s.replace('**', '* *')
while '*-' in s: s = s.replace('*-', '* -')
while '-*' in s: s = s.replace('-*', '- *')
mx = -float('inf')
# for item in s.split():
#     if mx < len(item):
#         for i in range(len(item) - 1):
#             if item[i] not in symbols:    
#                 tmp = [x for x in item.replace('*', '-').split('-') if len(x) != 0]
#                 flag = True
#                 sm = 0
#                 for j in tmp:
#                     if j[0] == '0':
#                         flag = False
#                         break
#                     sm += len(j)
#                 if flag:
#                     mx = max(mx, sm + len(tmp) - 1)

for item in s.split():
    if len(item) < mx:
        continue
    for i in range(len(item) - 1):
        ps = item[i]
        if item[i] not in symbols and item[i] != '0':
            for j in range(i + 1, len(item)):
                ps += item[j]
                if item[j-1] in symbols and item[j] == '0':
                    break
                if ps[-1] not in symbols:
                    try:
                        eval(ps)
                        if len(ps) > mx:
                            print(ps)
                            mx = len(ps)
                    except:
                        continue
print(mx)
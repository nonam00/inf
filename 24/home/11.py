s = open('11.txt').readline()
letters = 'ABCDO'
for i in letters:
    for j in letters:
        if (i in 'AO' and j in 'AO') or (i in 'BCD' and j in 'BCD'):
            while i+j in s: s = s.replace(i+j, i + ' ' + j)

print(max(len(item) for item in s.split() if item[0] in 'BCD' and item[-1] in 'AO') / 2)
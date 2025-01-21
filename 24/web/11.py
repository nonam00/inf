s = open('24_18186.txt').readline()

for c in 'CDFGH': s = s.replace(c, 'B')
s = s.replace('E', 'A')
s = s.replace('BBA', 'X')
s = s.split('X')
m = max(len(item) for item in s) + 6
print(m)
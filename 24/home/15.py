s = open('15.txt').readline()
while 'PR' in s: s = s.replace('PR', 'P R')
while 'RP' in s: s = s.replace('RP', 'R P')
print(max(len(item) for item in s.split()))
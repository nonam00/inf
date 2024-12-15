s = open('20.txt').readline()
while 'PP' in s: s = s.replace('PP', 'P P')
print(max(len(item) for item in s.split()))
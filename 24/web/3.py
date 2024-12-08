s = open('3.txt').readline()
while 'ad' in s: s = s.replace('ad', 'a d')
while 'da' in s: s = s.replace('da', 'd a')
print(max(len(item) for item in s.split()))

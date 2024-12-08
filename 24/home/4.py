s = open('4.txt').readline()
s = s.replace('N', '*').replace('O', '*').replace('P', '*')
while '**' in s: s = s.replace('**', '* *')
print(max(len(item) for item in s.split()))
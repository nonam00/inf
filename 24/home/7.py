s = open('7.txt').readline()
s = s.replace('+', '*')
while '**' in s: s = s.replace('**', '* *')
mx = max(len(item) for item in s.split())
print(mx)
print([item for item in s.split() if len(item) == mx])
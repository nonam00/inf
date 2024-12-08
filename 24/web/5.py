from string import ascii_uppercase
s = open('5.txt').readline()
print(ascii_uppercase)

sogl = 'CBDFGHJKLMNPQRSTVWXYZ'
gl = 'AEIOUY'

for c in sogl: s = s.replace(c, '1')
for c in gl: s = s.replace(c, '2')

while '12' in s: s = s.replace('12', '*')
while '1' in s: s = s.replace('1', ' ')
while '2' in s: s = s.replace('2', ' ')

print(max(len(item) for item in s.split()))

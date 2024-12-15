s = open('19.txt').readline()
s = s.split('T')
mx = -float('inf')
for i in range(len(s) - 100):
    sm = sum(len(item) for item in s[i:i+101])
    mx = max(mx, sm)
print(mx + 100)
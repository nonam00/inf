s = open('11.txt').readline()
mx = -float('inf')
n = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        n += 1
        mx = max(n, mx)
    else:
        n = 1

print(mx)
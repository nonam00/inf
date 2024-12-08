s = open('2.txt').readline()
letters = 'ABC'
nums = '89'
mx = -float('inf')
count = 1
for i in range(len(s) - 1):
    if (s[i] in letters and s[i + 1] not in letters) or (s[i] in nums and s[i + 1] not in nums):
        count += 1
        mx = max(mx, count)
    else:
        count = 1
print(mx)
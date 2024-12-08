s = open("2.txt").readline()
while 'CD' in s: s = s.replace('CD', 'C D')
s = s.split(' ')
# print(max(sum(len(kusok) for kusok in s)))
mx = -float('inf')
for i in range(len(s) - 160):
    sm = sum(len(item) for item in s[i:i+161])
    n = max(m,sm)
# # for i in range(len(s) + 1):
# #     for j in range(i + 1, len(s)):
# #         if s[i:j+1].count('CD') == 160:
# #             mx = max(mx, len(s[i n:j+1]))
# # print(mx)
# print(max(len(kusok) for i in s[i:i+3] for i in range(len(s - 3))))

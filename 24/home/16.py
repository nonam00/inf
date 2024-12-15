s = open('16.txt').readline()
mx = -float('inf')
st = ''
for i in range(len(s)):
    st += s[i]
    while st.count('X') > 1 or st.count('Y') > 1: st = st[1:]
    if st.count('X') == 1 and st.count('Y') == 1:
        mx = max(mx, len(st))
print(mx)
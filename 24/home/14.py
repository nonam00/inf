s = open('12.txt').readline()
for i in range(0, 10):
    for j in range(0, 10):
        if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
            while str(i)+str(j) in s:
                s = s.replace(str(i) + str(j), str(i) + ' ' + str(j))

print(max(len(item) for item in s.split()))
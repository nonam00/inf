from itertools import product

count = 0
for num in list(product('01234567', repeat=5)):
    if num[0] != '0' and num.count('6') == 1:
        pos = num.index('6')
        if pos == 0:
            if int(num[pos + 1]) % 2 == 0:
                count += 1
        elif pos == len(num) - 1:
            if int(num[pos - 1]) % 2 == 0:
                count += 1
        else:
            if int(num[pos - 1]) % 2 == 0 and int(num[pos + 1]) % 2 == 0:
                count += 1
                print(num, pos)
print(count)

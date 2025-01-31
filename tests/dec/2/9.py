count = 0
for line in open('9.txt'):
    numbers = [int(n) for n in line.split()]
    p2 = [x for x in numbers if numbers.count(x) == 2]
    np = [x for x in numbers if numbers.count(x) == 1]
    if len(p2) == 6 and len(np) == 1:
        if (max(p2) + min(p2)) / 2 < np[0]:
            count += 1
print(count)
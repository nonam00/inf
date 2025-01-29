from itertools import permutations
def check(a, b, c): return a ** 2 + b ** 2 == c ** 2
count = 0
for line in open('14.txt'):
    nums = [int(i) for i in line.split(';')]
    n2 = list(set([i for i in nums if nums.count(i) == 2]))
    if len(n2) == 3 and any(check(*i) for i in permutations(n2, r=3)):
        count += 1
print(count)

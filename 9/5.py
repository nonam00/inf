from itertools import permutations
def check(arr, ixs):
    return f(arr[ixs[0]], arr[ixs[1]]) and f(arr[ixs[2]], arr[ixs[3]])
def f(n,m): return (n + m) % 2 != 0
sm = 0
for line in open('5.txt'):
    nums = [int(i) for i in line.split()]
    n3 = list(set([i for i in nums if nums.count(i) == 3]))
    n2 = list(set([i for i in nums if nums.count(i) == 2]))
    if len(n3) == 1 and len(n2) == 2:
        nums.sort()
        if any(check(nums, ixs) for ixs in permutations([0, 1, 2, 3], r=4)):
            sm += sum(nums)
print(sm)


def p(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

nums = [int(s) for s in open('3.txt')]
arr = []

for i in range(len(nums) - 2):
    a = [nums[i], nums[i + 1], nums[i + 2]]
    if all('3' in str(n) for n in a):
        sm = sum(a)
        if p(sm):
            arr.append(sm)
print(len(arr), min(arr))
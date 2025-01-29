nums = [int(i) for i in open('22.txt')]
mx = max(i for i in nums if abs(i) % 10 == 3)
arr = []
for i in range(len(nums) - 1):
    n1, n2 = nums[i], nums[i + 1]
    if (abs(n1) % 10 == 3) + (abs(n2) % 10 == 3) == 1:
        sm = n1 ** 2 + n2 ** 2
        if sm >= mx ** 2:
            arr.append(sm)
print(len(arr), max(arr))

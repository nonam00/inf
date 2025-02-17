nums = [int(s) for s in open('7.txt')]
arr = []
mx = max(i for i in nums if i % 100 == 15)
for i in range(len(nums) - 2):
    n1, n2, n3 = nums[i], nums[i +1], nums[i + 2]
    if (1000 <= n1 <= 9999) + (1000 <= n2 <= 9999) + (1000 <= n3 <= 9999) == 1:
        sm = n1 + n2 + n3
        if sm >= mx:
            arr.append(sm)
print(len(arr), max(arr))
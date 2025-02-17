nums = [int(s) for s in open('9.txt')]
arr = []
mx = max(i for i in nums if abs(i) % 100 == 54)
for i in range(len(nums) - 1):
    n1, n2 = abs(nums[i]), abs(nums[i + 1])
    if n1 % 10 == n2 % 10:
        sm = n1 + n2
        if sm <= mx:
            arr.append(max(nums[i], nums[i + 1]))
print(len(arr), max(arr))
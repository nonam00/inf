nums = [int(i) for i in open('21.txt')]
mx = max(i for i in nums if abs(i) % 100 == 54)
arr = []
for i in range(len(nums) - 1):
    n1 = nums[i]
    n2 = nums[i + 1]
    if abs(n1) % 10 == abs(n2) % 10:
        if abs(n1) + abs(n2) <= mx:
            arr.append(max(n1, n2))
print(len(arr), max(arr))

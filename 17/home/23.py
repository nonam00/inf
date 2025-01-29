nums = [int(i) for i in open('23.txt')]
mx = max(abs(i) for i in nums if i % 1001 == 0)
arr = []
for i in range(len(nums) - 1):
    n1, n2 = nums[i], nums[i+1]
    if 100 <= abs(n1) <= 999 or 100 <= abs(n2) <= 999:
        sm = n1 + n2
        if sm > mx:
            arr.append(sm)
print(len(arr), min(arr))

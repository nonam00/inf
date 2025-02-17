nums = [int(s) for s in open('1.txt')]
mx = max(abs(x) for x in nums if abs(x) % 1001 == 0)
arr = []

for i in range(len(nums) - 1):
    if 100 <= abs(nums[i]) <= 999 or 100 <= abs(nums[i + 1]) <= 999:
        sm = nums[i] + nums[i + 1]
        if sm > mx:
            arr.append(sm)
print(len(arr), min(arr))

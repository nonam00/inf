nums = [int(s) for s in open('5.txt')]
mx = max([i for i in nums if i % 17 == 0])
arr = []
for i in range(len(nums) - 1):
    sm = nums[i] + nums[i + 1]
    if sm > mx:
        arr.append(sm)
print(len(arr), max(arr))
nums = [int(i) for i in open('20.txt')]
mn = min(nums)
arr = []
for i in range(len(nums) - 1):
    if nums[i] % 117 == mn or nums[i + 1] % 117 == mn:
        arr.append(nums[i] + nums[i + 1])
print(len(arr), max(arr))

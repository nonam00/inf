nums = [int(i) for i in open('17.txt')]
mn = min(nums)
arr = []
for i in range(len(nums) - 1):
    if nums[i] % 111 == mn or nums[i + 1] % 111 == mn:
        arr.append(nums[i] + nums[i + 1])
print(len(arr), min(arr))

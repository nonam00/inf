nums = [int(i) for i in open('12.txt')]
mn = min(i for i in nums if 100 <= i <= 999 and i % 10 == 5)
arr = []
for i in range(len(nums) - 1):
    if 100 <= nums[i] <= 999 or 100 <= nums[i + 1] <= 999:
        sm = nums[i] + nums[i + 1]
        if sm % mn == 0:
            arr.append(sm)

print(len(arr), max(arr))


nums = [int(x) for x in open("4.txt")]
mn = min(abs(x) for x in nums)
arr = []
for i in range(len(nums) - 1):
    if (nums[i] < 0) + (nums[i + 1] < 0) == 1:
        summ = nums[i] + nums[i + 1]
        if summ > 0 and summ % mn == 0:
            arr.append(summ)
print(len(arr), max(arr))

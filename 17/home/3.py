nums = [int(x) for x in open("3.txt")]
mx = max(x for x in nums if 10 <= x <= 99)
arr = []
for i in range(len(nums) - 1):
    if (10 <= nums[i] <= 99) + (10 <= nums[i+1] <= 99) == 1:
        summ = nums[i] + nums[i+1]
        if summ % mx == 0:
            arr.append(summ)
print(len(arr), max(arr))

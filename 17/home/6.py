nums = [int(x) for x in open("6.txt")]
mn = min(x for x in nums if (100 <= x <= 999) and (x % 10 == 5))
arr = []
for i in range(len(nums) - 1):
    if (100 <= nums[i] <= 999) or (100 <= nums[i + 1] < 999):
        summ = nums[i] + nums[i + 1]
        if summ % mn == 0:
            arr.append(summ)

print(len(arr), max(arr))

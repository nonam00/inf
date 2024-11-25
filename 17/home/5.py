nums = [int(x) for x in open("5.txt")]
mx = max(x for x in nums if 100 <= abs(x) <= 999)
arr = []
for i in range(len(nums) - 1):
    if (100 <= abs(nums[i]) <= 999) + (100 <= abs(nums[i + 1]) <= 999) == 1:
        summ = nums[i] + nums[i+1]
        if summ < mx:
            arr.append(summ)
print(len(arr), max(arr))

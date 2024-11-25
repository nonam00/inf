nums = [int(x) for x in open("9.txt")]
arr = []
mx = max(x for x in nums if x % 17 == 0)
for i in range(len(nums) - 1):
    summ = nums[i] + nums[i + 1]
    if summ > mx:
        arr.append(summ)
print(len(arr), max(arr))

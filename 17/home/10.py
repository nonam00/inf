nums = [int(x) for x in open("10.txt")]
arr = []
mx = max(x for x in nums if abs(x) % 10 == 3)
for i in range(len(nums) - 1):
    n1 = abs(nums[i])
    n2 = abs(nums[i + 1])
    if (n1 % 10 == 3) + (n2 % 10 == 3) == 1:
        summ = n1 ** 2 + n2 ** 2 
        if summ>= mx ** 2:
            arr.append(summ)
print(len(arr), max(arr))


def u(x):
    return 1000 <= x <= 9999

nums = [int(x) for x in open("7.txt")]
mx = max(x for x in nums if x % 100 == 15)
arr = []

for i in range(len(nums) - 2):
    n1, n2, n3 = nums[i], nums[i+1], nums[i+2]
    if u(n1) + u(n2) + u(n3) == 1:
        summ = n1 + n2 + n3
        if summ >= mx:
            arr.append(summ)
print(len(arr), max(arr))


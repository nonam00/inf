nums = [int(s) for s in open('6.txt')]
mx = max(i for i in nums if abs(i) % 10 == 3)
arr = []
for i in range(len(nums) - 1):
    if (abs(nums[i]) % 10 == 3) + (abs(nums[i + 1]) % 10 == 3) == 1:
        sm = nums[i] ** 2 + nums[i + 1] ** 2
        if sm > mx ** 2:
            arr.append(sm)
print(len(arr), max(arr))

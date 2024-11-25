nums = [int(x) for x in open('3.txt')]
mx = max(x for x in nums if abs(x) % 10 == 3 and 100 <= abs(x) <= 999)
r = []
for i in range(len(nums) - 2):
    u1 = abs(nums[i]) % 10 == 3 and 100 <= abs(nums[i]) <= 999
    u2 = abs(nums[i + 1]) % 10 == 3 and 100 <= abs(nums[i + 1]) <= 999
    u3 = abs(nums[i + 2]) % 10 == 3 and 100 <= abs(nums[i + 2]) <= 999
    if u1 or u2 or u3:
        if (nums[i] + nums[i + 1] + nums[i + 2]) < mx:
            r.append(nums[i] + nums[i + 1] + nums[i + 2])

print(len(r), max(r))


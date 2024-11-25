nums = [int(x) for x in open("4.txt")]
mx = max(x for x in nums if abs(x) % 100 = 13)
for i in range(len(a) - 2):
    u1 = 100 <= abs(nums[i]) <= 999
    u2 = 100 <= abs(nums[i + 1]) <= 999
    u3 = 100 <= abs(nums[i + 2]) <= 999
    if (u1 + u2 + u3) == 2:
        if (nums[i] + nums[i + 1] + nums[i + 2]) <= mx:
            r.append(nums[i] + nums[i + 1] + nums[i + 2])

print(len(r), max(r))

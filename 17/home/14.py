def p(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
nums = [int(i) for i in open('14.txt')]
mx = max(i for i in nums if abs(i) % 100 == 17)
arr = []
for i in range(len(nums) - 1):
    if (p(nums[i]) + p(nums[i + 1])) == 1:
        if (nums[i] + nums[i + 1]) % mx == 0:
            arr.append(nums[i] * nums[i + 1])

print(len(arr), max(arr))

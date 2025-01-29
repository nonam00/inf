def p(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
nums = [int(i) for i in open('11.txt')]
arr = []
for i in range(len(nums) - 2):
    if '3' in str(nums[i]) and '3' in str(nums[i + 1]) and '3' in str(nums[i + 2]):
        sm = nums[i] + nums[i + 1] + nums[i + 2]
        if p(sm):
            arr.append(sm)
print(len(arr), min(arr))

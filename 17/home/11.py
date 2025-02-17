import sys
from functools import lru_cache
sys.set_int_max_str_digits(100000000)
@lru_cache(None)
def p(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
nums = [int(i) for i in open('11.txt')]
arr = []
mx = max(i for i in nums if abs(i) % 100 == 17)
for i in range(len(nums) - 1):
    if (p(nums[i])) + (p(nums[i + 1])) == 1:
        if (nums[i] + nums[i + 1]) % mx == 0:
            arr.append(nums[i] * nums[i + 1])
print(len(arr), max(arr))
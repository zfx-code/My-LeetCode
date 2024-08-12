"""
滑动窗口, 对应两个指针(行为)
不够先赚钱, 够了再花钱, 重复
"""

def minSubArrayLen(target: int, nums) -> int:
    n = len(nums)
    ans = n + 1
    # [i, j]
    i = 0 
    # j先动, 找到满足条件的i再动
    s = 0
    for j in range(n):
        s += nums[j]

        while s >= target:
            ans = min(ans, j - i + 1)
            s -= nums[i]
            i += 1 

    if ans == n + 1:
        return 0
    return ans

target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))
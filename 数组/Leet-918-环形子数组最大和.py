"""
给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。

环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。

子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 合并起来切一刀, 再做dp (O(n^2))
        # 分别以0, 1,..., n-1作为开头
        n = len(nums)

        # 最大环形子数组和 = max(maxSum, total - minSum)
        maxSum = nums[0]
        pre = nums[0]
        total = nums[0]
        for i in range(1, n):
            total += nums[i]
            # 是否包含<i的曾经
            if pre > 0:
                pre += nums[i % n]
            else:
                pre = nums[i % n]
            maxSum = max(maxSum, pre)
        
        pre = nums[0]
        minSum = nums[0]
        for i in range(1, n):
            # 是否包含<i的曾经
            if pre < 0:
                pre += nums[i % n]
            else:
                pre = nums[i % n]
            minSum = min(minSum, pre)

        # 均小于0
        if maxSum < 0:
            return maxSum
        
        return max(maxSum, total - minSum)


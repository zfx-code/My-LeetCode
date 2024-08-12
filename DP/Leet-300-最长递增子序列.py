"""
300. 最长递增子序列

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列

贪心 + 二分
"""
import bisect 

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i]表示以i[结尾], 的最长严格递增子序列长度
        # dp = [1 for i in range(n)]
        # dp[0] = 0 
        # 方法二又给我上课了，一个新员工一个老员工价值相当，老员工就可以走了，因为新员工被榨取的剩余空间更多。
        
        # 更快的dp, 二分找插入位置
        # dp[i]表示长度为i的严格递增子序列的最小数
        # eg: [1,4,5,2] dp[2] = 4 -> dp[2] = 2
        dp = [nums[0]]

        max_L = 1
        # 一直到 max_L, dp都保持递增
        for i in range(1, n):
            # 需要修改/添加一个值
            # 找到一个位置j使得, dp[j-1] <= nums[i] < dp[j]
            # 更新dp[j] = nums[i]
            j = bisect.bisect_left(dp, nums[i])
            # 找不到, 可以放在最后的位置, 长度+1
            if j == len(dp):
                dp.append(nums[i])
            # nums[i]在长度j那里更小, 更新
            else:
                dp[j] = nums[i]
        
        return len(dp)


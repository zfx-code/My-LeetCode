"""
560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：


"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # pre[i]为[0:i)的和
        n = len(nums)
 
        # 子数组不必连续
        pre = 0
        hashtable = dict()
        hashtable[0] = 1
        # 要找pre[i]-pre[j - 1] = k
        # pre[j - 1] = pre[i] - k
        ans = 0
        # 考虑以i结尾的和为k的连续子数组只要考虑前缀和为pre[i] - k的pre[j]
        for i in range(n):
            pre += nums[i]
            if pre - k in hashtable:
                ans += hashtable[pre - k]
            if pre not in hashtable:
                hashtable[pre] = 1
            else:
                hashtable[pre] += 1 
        
        return ans

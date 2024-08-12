"""
1248. 统计「优美子数组」
给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中 「优美子数组」 的数目。
"""

class Solution:
    def numberOfSubarrays_method1(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        # odd[i]表示第i个奇数的下标
        # [left, right] = [odd[i], odd[i + k - 1]]
        # 对第i个奇数, 前一个奇数下标是odd[i - 1]
        # 则(odd[i - 1], odd[i])里全是偶数
        # 同理(odd[i + k - 1], odd[i + k])也全是偶数
        # 对第i个奇数, 能构成可行的解是(odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        # odd: cnt + 2(奇数个数+2)
        odd = [-1]
    
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        # 注意边界
        odd.append(n)
    
        ans = 0
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        
        return ans
    
    # 前缀和+差分
    def numberOfSubarrays_method2(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        """
        考虑以i结尾的[优美子数组的个数], 需要统计下标j的个数, 使得[j, i]闭区间内奇数的个数的k个
        定义pre[i]为[0, i]中奇数的个数:
            pre[i + 1] = pre[i] + (nums[i] % 2)
        则[j, i]中k个奇数 => pre[i] - pre[j - 1] == k 
        即固定i, 需要找满足pre[j - 1] = pre[i] - k的j[的个数]即可
        注意, 为了只考虑左边, 建立pre和更新ans是同时的(不会预处理)
        只用一个变量即可
        """
        # cnt 是记录pre[i]出现的次数
        odd = 0 
        ans = 0 
        cnt = [0 for _ in range(n + 1)]
        cnt[0] = 1 

        for i in range(n):
            odd += nums[i] & 1
            ans += cnt[odd - k] if odd >= k else 0 
            cnt[odd] += 1
        
        
        return ans


"""
229. 多数元素 II

给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

示例 1：

输入：nums = [3,2,3]
输出：[3]
示例 2：

输入：nums = [1]
输出：[1]
示例 3：

输入：nums = [1,2]
输出：[1,2]
 

提示：

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        消消乐 - 摩尔投票法
        初始化候选者cand和票数cnt 
        遍历元素, 匹配上  => cnt++
                 cnt = 0 => 更换cand 
                 未匹配  => cnt--
        > n // (m + 1) 最多有m可能的候选人, 最后需要验证
        且m候选人有重复的, 需要去重使用if else计数验证
        """

        # 大于 n // 3的最多2个
        n = len(nums)
        ans = []
        if n == 0:
            return ans 
        
        # 候选人+票数
        cand1, cand2 = nums[0], nums[0]
        cnt1, cnt2   = 0, 0

        # (1) 配对阶段
        for x in nums:
            if cand1 == x:
                cnt1 += 1 
                continue 
            
            if cand2 == x:
                cnt2 += 1 
                continue 
            
            # 更换候选人1
            if cnt1 == 0:
                cand1 = x 
                cnt1 += 1 
                continue 
            
            # 更换候选人2 
            if cnt2 == 0:
                cand2 = x 
                cnt2 += 1 
                continue 
            
            # 抵消
            cnt1 -= 1 
            cnt2 -= 1 

        # (2) 计数阶段 - 验证候选人的票是否大于n//3
        cnt1, cnt2 = 0, 0 
        for x in nums:
            if cand1 == x:
                cnt1 += 1 
            # 候选人可能一样, 必须用else语句
            elif cand2 == x:
                cnt2 += 1 
        
        if cnt1 > n // 3:
            ans.append(cand1)
        if cnt2 > n // 3:
            ans.append(cand2)
        
        return ans
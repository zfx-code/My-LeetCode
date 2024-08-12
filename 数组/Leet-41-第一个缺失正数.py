"""
Leet-41-第一个缺失正数

给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

核心:
    原地Hash, Hash(nums[i]) = nums[i] - 1
"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # 首先断言, ans in [1, n + 1]
        n = len(nums)

        # 原地hash, 数组下标为i的位置应该存下i + 1
        # f(nums[i]) = nums[i] - 1(hash规则, 决定nums[i]应该存在哪里)
        # 因此[0, n - 1] -> [1, n]

        for i in range(n):
            # 他是可以存到某个位置的
            # 如果本来就是应该的位置, 就不用交换了
            while nums[i] >= 1 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 应该的位置j
                j = nums[i] - 1 
                # 交换
                nums[i], nums[j] = nums[j], nums[i] 

                # 交换完了新的nums[i]也许还可以能存到别的位置
                # 这步while就可以合并到上一步的if中
                # while nums[i] >= 1 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                #     # 应该的位置j
                #     j = nums[i] - 1 
                #     # 交换
                #     nums[i], nums[j] = nums[j], nums[i] 
                # 此时位置i的元素要么已经是i+1, 要么不在[1, n + 1]范围内
                # 可以往后走 
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

"""
448. 找到所有数组中消失的数字

给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 原地哈希 
        for a in nums:
            nums[abs(a) - 1] = - abs(nums[abs(a) - 1])
        
        n = len(nums)
        # 没被占过, 没出现
        ans = [i + 1 for i in range(n) if nums[i] > 0]

        return ans

"""
442. 数组中重复的数据

给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = []
        for x in nums:
            idx = abs(x) - 1 
            if nums[idx] < 0:
                ans.append(idx + 1)
            else:
                nums[idx] = - nums[idx]
        
        return ans

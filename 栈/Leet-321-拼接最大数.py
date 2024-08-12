"""
321. 拼接最大数

给你两个整数数组 nums1 和 nums2，它们的长度分别为 m 和 n。数组 nums1 和 nums2 分别代表两个数各位上的数字。同时你也会得到一个整数 k。

请你利用这两个数组中的数字中创建一个长度为 k <= m + n 的最大数，在这个必须保留来自同一数组的数字的相对顺序。

返回代表答案的长度为 k 的数组。

 

示例 1：

输入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
输出：[9,8,6,5,3]
示例 2：

输入：nums1 = [6,7], nums2 = [6,0,4], k = 5
输出：[6,7,6,0,4]
示例 3：

输入：nums1 = [3,9], nums2 = [8,9], k = 3
输出：[9,8,9]
"""

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 子函数: 从1个数组中抽取s位字典序最大
        def sub_s(nums, s):
            n = len(nums)
            if n <= s:
                return nums[:]
            # 维护单调递减栈 
            # 最多只能pop掉n - s个(留s个)
            pop = n - s 
            stack = []
            for i in range(n):
                while len(stack) > 0 and nums[i] > stack[-1] and pop > 0:
                    stack.pop()
                    pop -= 1
                stack.append(nums[i])
            
            # 截取掉前s个
            return stack[:s]
        
        # 字典序合并两个数组
        def merge(A, B):
            ans = []
            while A or B:
                bigger = max(A, B)
                ans.append(bigger[0])
                # A/B会跟着变化
                bigger.pop(0)
            return ans

        # 
        ans = [0 for _ in range(k)]
        n, m = len(nums1), len(nums2)
        # s个来自nums1
        for s in range(max(0, k - m), 1 + min(k, n)):
            nums1_sub = sub_s(nums1, s)
            nums2_sub = sub_s(nums2, k - s)
            
            print(f"s: {s}")
            print(f"nums1_sub: {nums1_sub}")
            print(f"nums2_sub: {nums2_sub}")
            tmp = merge(nums1_sub, nums2_sub)
            print(f"tmp: {tmp}")
            # 合并是字典序, 而非普通的有序合并
            # python特性
            ans = max(ans, tmp)
        
        return ans



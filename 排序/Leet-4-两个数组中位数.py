"""
4. 寻找两个正序数组的中位数

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/2641371/javapython3cshuang-zhi-zhen-er-fen-cha-z-ftlo
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        # 额外加一个数判定
        INT_MAX = 1000001
        nums1.append(INT_MAX)
        nums2.append(INT_MAX)

        k = (m + n + 1) // 2 

        idx1, idx2 = 0, 0
        mid_is_nums1 = False 

        while True:
            # nums1走到头了, 剩下找nums2要
            if idx1 == m:
                idx2 += k - 1  
                break 
            
            # nums2走到头 
            if idx2 == n:
                idx1 += k - 1 
                mid_is_nums1 = True
                break 
            
            # 单独处理最后1个数 
            if k == 1:
                mid_is_nums1 = nums1[idx1] < nums2[idx2] 
                break 
            
            # 各取出k/2个, 扔掉结尾小的那一组
            half = k // 2
            mid1 = min(idx1 + half, m) - 1 
            mid2 = min(idx2 + half, n) - 1 

            # 扔掉[idx1, mid1]
            if nums1[mid1] < nums2[mid2]:
                k -= mid1 - idx1 + 1 
                idx1 = mid1 + 1 
            else: 
                k -= mid2 - idx2 + 1 
                idx2 = mid2 + 1 
        
        # 奇数
        if (m + n) & 1:
            return nums1[idx1] if mid_is_nums1 else nums2[idx2]
        
        # 偶数平均
        if mid_is_nums1:
            return 0.5 * (nums1[idx1] + min(nums1[idx1 + 1], nums2[idx2]))
        return 0.5 * (nums2[idx2] + min(nums2[idx2 + 1], nums1[idx1]))





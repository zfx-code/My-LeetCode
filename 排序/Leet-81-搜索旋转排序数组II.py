"""
81. 搜索旋转排序数组 II

已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

你必须尽可能减少整个操作步骤。

进一步: 
    https://leetcode.cn/problems/search-rotate-array-lcci/description/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 二分, 找值是否存在的
        # 问题出在旋转点在相同元素的时候会导致首尾相同, 无法判断
        # 预处理恢复二段性
        # eg: [0,1,2,2|,2,3,4,5] 旋转后 [2,3,4,5,0,1]2,2
        # 最后的2,2就是干扰项

        n = len(nums)
        l, r = 0, n - 1
        # 恢复二段性
        while l < r and nums[0] == nums[r]:
            r -= 1 
        
        # (1) 第一次二分, 找旋转点(间断点)
        # 大于现在nums[0]的最大值
        while l < r:
            """
            mid = left + (right - left) / 2还是mid = left + (right - left + 1) / 2是完全不同的
            一个取得是靠左边的中位数，一个取得是靠右的中位数
            结论，循环体中有令left = mid，一定选第二种，否则选第一种
            """
            mid = l + (r - l + 1) // 2 
            if nums[mid] >= nums[0]:
                l = mid 
            else:
                r = mid - 1
        # l = r, 是旋转点前, 即[0, l]是一段递增, [l+1, n - 1]是一段递增

        # (2) 分别在两段利用二分找target
        def bin_search(nums, l, r, target):
            if l > r:
                return False
            while l < r:
                mid = l + (r - l) // 2 
                if nums[mid] >= target:
                    r = mid 
                else:
                    l = mid + 1 

            return nums[l] == target
        
        return bin_search(nums, 0, r, target) or bin_search(nums, r + 1, n - 1, target)
        

         

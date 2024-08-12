"""
34. 在排序数组中查找元素的第一个和最后一个位置

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        left, right = 0, n - 1
        # 找第一个 >= target的结果
        while left < right:
            mid = left + ((right - left) >> 1)
            # print(left, right, mid)
            # mid可能是个解
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if nums[right] != target:
            return [-1, -1]
        ans = [right]

        left, right = 0, n - 1
        # 找第一个 > target的结果(保证有target), 再-1(最后一个 = target)
        while left < right:
            mid = left + ((right - left) >> 1)
            # print(left, right, mid)
            # mid可能是个解
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        # 卡边界, eg: [2, 2] target=2, right=1, 此时1就对了不用再-1
        if right - 1 >= 0 and nums[right] != target:
            ans.append(right - 1)
        else:
            ans.append(right)

        return ans
    
s = Solution()
nums = [5,7,7,8,8,10]
target = 8

print(s.searchRange(nums=nums, target=target))




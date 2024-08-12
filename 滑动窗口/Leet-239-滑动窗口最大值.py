"""
Leet-239-滑动窗口最大值

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""

from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        from collections import deque 

        # 存的是下标
        # 满足是一个单调递减, front存max, back存min
        window = deque()
        n = len(nums)
        ans = []

        # 初始化k个整数(为一个窗口)
        for i in range(k):
            # 当新来的数 > back时, 扔掉back的, 直到新来的数 < back 或队列为空
            while len(window) > 0 and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)
        
        ans.append(nums[window[0]])

        # 移动窗口, 新元素下标从k开始
        # i作为窗口结尾[i - k + 1, i]
        for i in range(k, n):
 
            # 把已经不在窗口里的front扔掉
            if len(window) > 0 and window[0] <= i - k:
                window.popleft()
            while len(window) > 0 and nums[i] > nums[window[-1]]:
                window.pop()

            window.append(i)
            ans.append(nums[window[0]])
        
        return ans 

s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3 

s.maxSlidingWindow(nums=nums, k=k)










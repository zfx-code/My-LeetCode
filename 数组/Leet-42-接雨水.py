"""
42. 接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

1表示柱子的位置
0表示接水的位置
# # # # # # # 1 # # # #
# # # 1 0 0 0 1 1 0 1 #
# 1 0 1 1 0 1 1 1 1 1 1

解法2: 按列求
想要求每一列的水, 需要3个指标[left, cur, right]
能装水取min(left, right) - cur
需要关注到底如何取left和right
注意left, right不是i-1, i+1
而是一直找到最高的, 当做i-1, i+1(因为只需要考虑i位置)
因此需要去掉中间无关的墙

按高度划分, [left, right]必有1高1矮, 取矮的为low, 则表示为[low, cur, low]
(1) low > cur: 能装low - cur
(2) low < cur: 装不了
(3) low = cur: 装不了

解法3 维护最大left, right:
内存关于j的循环, 找left, right最大值的部分可以优化

"""

class Solution:
    # 按列找, 超时
    def trap_method2(self, height: list[int]) -> int:
        """
        按高度划分, [left, right]必有1高1矮, 取矮的为low, 则表示为[low, cur, low]
        (1) low > cur: 能装low - cur
        (2) low < cur: 装不了
        (3) low = cur: 装不了
        """
        n = len(height)
        
        ans = 0
        # 最边上肯定装不了
        for i in range(1, n - 1):
            cur = height[i]
            # 找left最高
            left = 0
            for j in range(0, i):
                left = max(left, height[j])
            
            # 找right最高
            right = 0
            for j in range(i + 1, n):
                right = max(right, height[j])
            
            low = min(left, right)
            if low > cur:
                ans += low - cur
        
        return ans

    # 维护left, right
    def trap_method3(self, height: list[int]) -> int:
        """
        按高度划分, [left, right]必有1高1矮, 取矮的为low, 则表示为[low, cur, low]
        (1) low > cur: 能装low - cur
        (2) low < cur: 装不了
        (3) low = cur: 装不了
        """
        n = len(height)
        
        ans = 0
        # left[i]表示[1, i-1]闭区间的最大值
        left = [0] * n
        # right[i]表示[i+1, n-2]闭区间的最大值
        right = [0] * n

        for i in range(1, n - 1):
            left[i] = max(left[i - 1], height[i - 1])
            # right要反着做, 即n-2->n-3->...1
            right[n - 1 - i] = max(right[n - i], height[n - i])

        # 最边上肯定装不了
        for i in range(1, n - 1):
            cur = height[i]
            
            low = min(left[i], right[i])
            if low > cur:
                ans += low - cur
        
        return ans

    # 双指针, O(1)空间
    def trap_method4(self, height: list[int]) -> int:
        """
        按高度划分, [left, right]必有1高1矮, 取矮的为low, 则表示为[low, cur, low]
        (1) low > cur: 能装low - cur
        (2) low < cur: 装不了
        (3) low = cur: 装不了
        """
        n = len(height)
        
        ans = 0
        # left, right表示指针
        left, right = 0, n - 1
        # left_max, right_max表示左边右边的最大值
        left_max, right_max = height[left], height[right]
        left += 1
        right -= 1

        # 向中间移动, 每次动1边, left++ or right--

        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 每次动较小的
            if left_max < right_max:
                # 此时已经排除了(2)情况, 最差是+0
                # eg: [1, 2, 1]是不能装水的, 此时变成update
                # 1->2: [2, 2, 2]同样不能装水
                # left_max >= height[left]
                ans += left_max - height[left]
                left += 1 
            else:
                ans += right_max - height[right]
                right -= 1 
            
        return ans
    
    # 栈, 参考括号"()"匹配问题
    def trap_method4(self, height: list[int]) -> int:
        """
        括号 == 墙
        栈存下墙, 若新高度 < 栈顶, 可能有积水, push
        若新高度 > 栈顶, 已经是一段完整的积水, pop并计算
        """
        n = len(height)
        
        ans = 0
        
            
        return ans


s = Solution()
print(s.trap_method3(height=[0,1,0,2,1,0,1,3,2,1,2,1]))

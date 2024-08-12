"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积
"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # 以位置i为最矮柱子所能扩展到的最大面积
        # 向左向右, 寻找到比i高度低的位置left, right
        # 则宽为right-left+1
        n = len(heights)
        left = [0 for i in range(n)]
        right = [n - 1 for i in range(n)]

        stack = []
        # 正向找right
        for i in range(n):
            h = heights[i]
            # print("########################")
            # print(f"h: {h}, stack: {stack}")
            if len(stack) > 0 and heights[stack[-1]] > h:
                while len(stack) > 0 and heights[stack[-1]] > h:
                    j = stack.pop()
                    right[j] = i - 1 
            
            stack.append(i)
            # print(f"h: {h}, stack: {stack}")
        
        stack = []
        # 反向找left
        for i in range(n - 1, -1, -1):
            h = heights[i]
    
            if len(stack) > 0 and heights[stack[-1]] > h:
                while len(stack) > 0 and heights[stack[-1]] > h:
                    j = stack.pop()
                    left[j] = i + 1 
            stack.append(i)
        
        ans = 0 
        for i in range(n):
            ans = max(ans, heights[i] * (right[i] - left[i] + 1))
        
        return ans

"""

代码
85. 最大矩形

给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

 
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 以位置i为最矮柱子所能扩展到的最大面积
        # 向左向右, 寻找到比i高度低的位置left, right
        # 则宽为right-left+1
        n = len(heights)
        left = [0 for i in range(n)]
        right = [n - 1 for i in range(n)]

        stack = []
        # 正向找right
        for i in range(n):
            h = heights[i]
   
            while len(stack) > 0 and heights[stack[-1]] > h:
                j = stack.pop()
                right[j] = i - 1 
            
            stack.append(i)
            
        stack = []
        # 反向找left
        for i in range(n - 1, -1, -1):
            h = heights[i]
    
            while len(stack) > 0 and heights[stack[-1]] > h:
                j = stack.pop()
                left[j] = i + 1 
            stack.append(i)
        
        ans = 0 
        for i in range(n):
            ans = max(ans, heights[i] * (right[i] - left[i] + 1))
        
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # m行n列 
        m, n = len(matrix), len(matrix[0])

        s = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = 0 if matrix[i - 1][j - 1] == "0" else s[i - 1][j] + 1 
            print(s[i])
        
        ans = 0
        # 逐行处理
        # for i in range(1, m + 1): 
        #     ans = max(ans, self.largestRectangleArea(s[i][1:]))
        # 逐行处理
        for i in range(1, m + 1):
            cur = s[i]

            left = [0 for _ in range(n + 1)]
            right = [n + 1 for _ in range(n + 1)]

            stack = []
            # 更新left(left[i]表示左边第一个小于cur[j]的, 要排除)
            for j in range(1, n + 1):
                while len(stack) > 0 and cur[stack[-1]] > cur[j]:
                    right[stack.pop()] = j 
                stack.append(j) 
            
            stack = []

            for j in range(n, 0, -1):
                while len(stack) > 0 and cur[stack[-1]] > cur[j]:
                    left[stack.pop()] = j 

                stack.append(j) 
            
            for j in range(1, n + 1):
                ans = max(ans, cur[j] * (right[j] - left[j] - 1))

        return ans    

"""
306. 累加数

累加数 是一个字符串，组成它的数字可以形成累加序列。

一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。

给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。

说明：累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

 

示例 1：

输入："112358"
输出：true 
解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2：

输入："199100199"
输出：true 
解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
 

提示：

1 <= num.length <= 35
num 仅由数字（0 - 9）组成
 

进阶：你计划如何处理由过大的整数输入导致的溢出?
"""

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False 
        
        # 确定a, b后c=a+b是固定的, 高精模拟加法
        def check(a, b, c):
            res = []
            t = 0 
            i = 0 
            while i < len(a) or i < len(b):
                if i < len(a):
                    t += a[i]
                if i < len(b):
                    t += b[i]
                res.append(t % 10)
                t = t // 10
                i += 1
            
            if t > 0:
                res.append(1)
            
            if len(res) != len(c):
                return False 
            
            for i in range(len(c)):
                if res[i] != c[i]:
                    return False
            
            return True 

        # 当前决策到num[u]这一位, 枚举结束位置[u, n - 1]
        # 只枚举当前这个x的可能情况, 考虑满足是前两数的和(或先填充前两个数)
        # 特殊情况, 若num[u]=0, 则只能a=0
        def dfs(u, cur):
            m = len(cur)
            # 结束条件
            if u == n:
                return m >= 3 
            
            # 最大位置可能
            end = u + 1 if num[u] == "0" else n 

            tmp = []
            for i in range(u, end):
                # 数x对应的数组
                tmp = [int(num[i])] + tmp
                if m < 2 or check(cur[m - 2], cur[m - 1], tmp):
                    # 第i位已经确定了, 下次从i+1起步
                    if dfs(i + 1, cur + [tmp]):
                        return True 
            
            return False
        
        return dfs(0, [])

            

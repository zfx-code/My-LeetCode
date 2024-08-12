"""
131. 分割回文串

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 
回文串
 。返回 s 所有可能的分割方案。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
"""

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # 预处理[i, j]是否回文
        # f[i][j]表示[i, j]是否回文, 可使用递推
        # f[i + 1][j - 1] = 1 and s[i] = s[j] => f[i][j] = 1
        # 左端点i从大到小, 右端点j从小到大

        # j += 1, i在固定j情况下, i -= 1

        n = len(s)
        f = [[False for _ in range(n)] for _ in range(n)]

        for j in range(n):
            f[j][j] = True
            # 长度为2
            if j > 0:
                f[j - 1][j] = s[j - 1] == s[j]
            # 长度 > 2可以递推 
            for i in range(j - 2, -1, -1):
                f[i][j] = (s[i] == s[j] and f[i + 1][j - 1])
        
        """
        s:   待搜索字符串
        u:   s的分割起点 
        ans: 最终结果
        cur: 当前结果
        """

        def dfs(s, u, ans, cur):
            n = len(s)

            # 分割结束
            if u == n:
                print(cur)
                # copy, 否则cur自己会清空
                ans.append(cur[:])
            
            for i in range(u, n):
                # [u, i]这段可以构成回文, 递归下去
                if f[u][i]:
                    print(u, i)
                    cur.append(s[u:i + 1])
                    dfs(s, i + 1, ans, cur)
                    # 把刚加进来这段pop出去
                    cur.pop()
        
        # ans = [cur[i] for i in _]
        ans = []
        cur = []

        dfs(s, 0, ans, cur)

        return ans







"""
记忆化搜索
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        # (x0, y0)是起点
        # @lru_cache(None)
        def dfs(x, y):
            if memo[x][y] > 0:
                return memo[x][y]
            memo[x][y] = 1
            # 继续尝试走
            dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    memo[x][y] = max(memo[x][y], dfs(nx, ny) + 1)
            return memo[x][y]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans
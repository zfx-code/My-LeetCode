"""
Leet-994-腐烂的橘子

在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

"""


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 检查是否全是坏橘子
        # True: 全坏了
        # False: 还有好的
        def check(grid):
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return False 
            
            return True 
        
        if check(grid):
            return 0

        ans = 1 

        # 开始更新
        from queue import Queue
        # 队列里存的是坏橘子的坐标
        # 更新一次意味着清空队列
        q = Queue()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.put([i, j])
        
        dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while not q.empty():
            size = q.qsize()

            for _ in range(size):
                x, y = q.get()

                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    # 影响的新位置是新鲜橘子
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.put([nx, ny])
                
            # 影响了一轮
            if check(grid):
                return ans 
            ans += 1

        return -1 
        





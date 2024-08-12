"""
根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。

进阶：

1. 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
2. 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
"""

"""
规则简化
1. 1 + [2, 3]-1 = 1(还活)
2. 0 + 3-1      = 1(复活)
3. 0全死

注意到, 死的是无法影响其他细胞的
只需要让活的1去"影响"周围8细胞, +10
十位存着新的周围活细胞, eg: 41表示原来活着, 现在周围4个活细胞 -> 死了
"""

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # (x, y)处的活细胞影响周围8个结果
        def affect(x, y):
            for i in [x - 1, x, x + 1]:
                for j in [y - 1, y, y + 1]:
                    # 越界标识 + 不影响自己
                    if i < 0 or i > m - 1 or j < 0 or j > n - 1 or (i == x and j == y):
                        continue
                    board[i][j] += 10

        for i in range(m):
            for j in range(n):
                # 当前状态是活的
                if board[i][j] % 10 == 1:
                    affect(i, j)
        
        # 再遍历一次, 更新所有状态
        for i in range(m):
            for j in range(n):
                state = board[i][j]

                # 一定活
                if state // 10 == 3:
                    board[i][j] = 1
                elif state // 10 == 2 and state % 10 == 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        
        print(board)


s = Solution()
s.gameOfLife(board=board)

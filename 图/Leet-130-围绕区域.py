"""
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

L200. 岛屿数量 （Easy）
463. 岛屿的周长 （Easy）
695. 岛屿的最大面积 （Medium）
827. 最大人工岛 （Hard）

输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""

# 围绕区域
def solve(board: list[list[str]]) -> int:
    # 判断坐标 (r, c) 是否在网格中
    def inArea(board: list[list[str]], r: int, c: int):
        return 0 <= r and r < len(board) and 0 <= c and c < len(board[0])

    # dfs处理网格问题的基本框架, 需要加标记vis
    def dfs(board: list[list[str]], r: int, c: int):
        # 判断 base case
        # 如果坐标 (r, c) 超出了网格范围，直接返回
        if inArea(board, r, c) == False:
            return
        
        # 不是"O"
        if board[r][c] != "O":
            return 
        
        # "?"表示留下的"O"
        board[r][c] = "?"

        #  访问上、下、左、右四个相邻结点
        dfs(board, r - 1, c)
        dfs(board, r + 1, c)
        dfs(board, r, c - 1)
        dfs(board, r, c + 1)
    
    # n行m列
    n = len(board)
    m = len(board[0])
    # 每找到一个"1", 岛屿+1, 因为会把连通的全部标记成"2"
    for r in range(n):
        # 所有边界点
        c_range = [i for i in range(m)]
        if r not in [0, n - 1]:
            c_range = [0, m - 1]
        
        for c in c_range:
            # 边界的"O"作为起点
            if board[r][c] == "O":
                dfs(board, r, c)
    
    # "?"只能是"O", 其他全是"X"
    for r in range(n):
        for c in range(m):
            if board[r][c] == "?":
                board[r][c] = "O"
            else:
                board[r][c] = "X"

    print(board)

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

solve(board=board)
"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

思路:
等价于找连通集合

在 LeetCode 中，「岛屿问题」是一个系列系列问题，比如：

L200. 岛屿数量 （Easy）
463. 岛屿的周长 （Easy）
695. 岛屿的最大面积 （Medium）
827. 最大人工岛 （Hard）

作者：nettee
链接：https://leetcode.cn/problems/number-of-islands/solutions/211211/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/
来源：力扣（LeetCode）

eg:
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
"""
# 判断坐标 (r, c) 是否在网格中
def inArea(grid: list[list[str]], r: int, c: int):
    return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])

# dfs处理网格问题的基本框架, 需要加标记vis
def dfs(grid: list[list[str]], r: int, c: int):
    # 判断 base case
    # 如果坐标 (r, c) 超出了网格范围，直接返回
    if inArea(grid, r, c) == False:
        return
    
    # 不是岛屿
    if grid[r][c] != "1":
        return 
    
    # "2"表示已经走过
    grid[r][c] = "2"

    #  访问上、下、左、右四个相邻结点
    dfs(grid, r - 1, c);
    dfs(grid, r + 1, c);
    dfs(grid, r, c - 1);
    dfs(grid, r, c + 1);

def numIslands(grid: list[list[str]]) -> int:
    # 判断坐标 (r, c) 是否在网格中
    def inArea(grid: list[list[str]], r: int, c: int):
        return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])

    # dfs处理网格问题的基本框架, 需要加标记vis
    def dfs(grid: list[list[str]], r: int, c: int):
        # 判断 base case
        # 如果坐标 (r, c) 超出了网格范围，直接返回
        if inArea(grid, r, c) == False:
            return
        
        # 不是岛屿
        if grid[r][c] != "1":
            return 
        
        # "2"表示已经走过
        grid[r][c] = "2"

        #  访问上、下、左、右四个相邻结点
        dfs(grid, r - 1, c)
        dfs(grid, r + 1, c)
        dfs(grid, r, c - 1)
        dfs(grid, r, c + 1)
    
    ans = 0

    # 每找到一个"1", 岛屿+1, 因为会把连通的全部标记成"2"
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                dfs(grid, r, c)
                ans += 1
        
    return ans 

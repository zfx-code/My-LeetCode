"""
回溯类型题

n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

任意两个皇后不能再同一行/列/斜线上
"""

# 检查该方案是否合法
# board = [[..0...1], [...]
# 1表示是皇后
def check(board):
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            # 不是皇后 
            if board[i][j] == ".":
                continue
                
            # 以此皇后判断, 只要搜后边即可, 不用往前看
            # (1) 行
            for k in range(i+1, n):
                # print(board[i][k])
                if board[k][j] == "Q":
                    return False 
            
            # (2) 列
            for k in range(j+1, n):
                # print(board[i][k])
                if board[i][k] == "Q":
                    return False 
            
            # (3) 斜对角线, 左右都要考虑
            for k in range(1, min(n-i, n-j)):
                if board[i+k][j+k] == "Q":
                    return False 
            
            for k in range(1, min(n-i, j+1)):
                if board[i+k][j-k] == "Q":
                    return False 
    return True 

ans = 0
# 当前最后一个queen是r, 任何>r的位置不可能有queen
# 为第r行分配queen
def queen_dfs(board, r):
    global ans 
    n = len(board)
    # 已经有了n个queen
    if r == n :
        ans += 1
        # print(board)
        return
    # print(f"row : {r}")
    # 列
    for j in range(n):
        board[r][j] = "Q"
        # print(board)
        if check(board) == True:
            # print("yes")
            # 为下一行分配
            queen_dfs(board, r + 1)
        board[r][j] = "."  


def N_Queen(n):
    global ans 
    ans = 0
    # 棋盘, "Q" or "."
    board = [["." for j in range(n)] for i in range(n)]
    queen_dfs(board, 0)
    
    print(ans)

n = 8

N_Queen(n=n)

"""
Leet-17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
"""

def letterCombinations(digits: str) -> list[str]:
    if len(digits) == 0:
        return []

    hashtable = {
        "2" : "abc"
        , "3" : "def"
        , "4" : "ghi"
        , "5" : "jkl"
        , "6" : "mno"
        , "7" : "pqrs"
        , "8" : "tuv"
        , "9" : "wxyz"
    }

    ans = []

    # 考虑完下标是i(长度是i + 1)的部分
    def dfs(i, cur):
        # print(i, cur)
        nonlocal ans
        # 结束条件, 位数相同, i是当前的结果长度
        if i + 1 == len(digits):
            ans.append(cur)
            return 
        
        # dfs就是要考虑当前-i的全部可能
        n = len(hashtable[digits[i + 1]])
        # 这时的i + 1不会越界, 被i + 1限制住了
        for k in range(n):
            dfs(i + 1, cur + hashtable[digits[i + 1]][k])

    # 对第一位置遍历所有情况 
    for letter in hashtable[digits[0]]:
        dfs(0, letter)

    return ans

digits = "23"

print(letterCombinations(digits))


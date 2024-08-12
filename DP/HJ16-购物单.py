"""
华为笔试测试题: 购物单(动态规划)

王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。
王强查到了每件物品的价格（都是 10 元的整数倍），而他只有 N 元的预算。除此之外，他给每件物品规定了一个重要度，用整数 1 ~ 5 表示。他希望在花费不超过 N 元的前提下，使自己的满意度达到最大。
满意度是指所购买的每件物品的价格与重要度的乘积的总和，假设设第


输入描述：
输入的第 1 行，为两个正整数N，m，用一个空格隔开：

（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）


从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q


（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
"""

row1 = list(map(int, input().split(" ")))
# 钱数N, 物品个数m
N, m = row1

N = N // 10
# 邻接表存主件:附件
# 主件索引
main_vp = dict()
edges = [[] for _ in range(60)]
for j in range(m):
    # v: 价格
    # p: 重要度(1-5)
    # q: 主件(>0, 是q主件的附件)/主件(0)
    v, p, q = list(map(int, input().split(" ")))
    if q > 0:
        edges[q - 1].append([v//10, p])
    # 主件
    else:
        main_vp[j] = [v//10, p]

main_idxs = list(main_vp.keys())
# 主件件数
n = len(main_idxs)
"""
每个主件最多可以有2个附件
则状态为, 00, 01, 10, 11
分别对应1+0, 1+1, 1+1, 1+2

定义dp[i][j]为只考虑前i件主件, 预算为j时候最大的满意度 

考虑dp[i][j]时, 依赖dp[i-1]
若第i件自己就买不了了, dp[i][j] = dp[i-1][j]
能买第i件, 考虑上述4种情况取max 

"""

# dp[i][j], 前i个主件, 预算为j时候最大的满意度
dp = [[0 for _ in range(N + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, N + 1):
        # 当前考虑第i个物品(索引i - 1)
        idx = main_idxs[i - 1]
        v, p = main_vp[idx]

        dp[i][j] = dp[i - 1][j]
        # 买不起主件
        if j - v < 0:
            continue
        
        # 至少主件买得起, 看看附件可不可行
        # (1) 只买一个主件
        dp[i][j] = max(dp[i][j], dp[i - 1][j - v] + v * p)
 
        # 没有主件
        if len(edges[idx]) == 0:
            continue
        # (2) 买主件+第1个附件
        v1, p1 = edges[idx][0]
        if j - v - v1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - v - v1] + v * p + v1 * p1)
      
        # 只有1个附件
        if len(edges[idx]) == 1:
            continue
        
        # (3) 买主件+第2个附件
        v2, p2 = edges[idx][1]
        if j - v - v2 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - v - v2] + v * p + v2 * p2)
        
        
        # (4) 买主件+第1第2附件
        if j - v - v1 - v2 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - v - v1 - v2] + v * p + v1 * p1 + v2 * p2)
        

# print("###########")
# print(edges)
# print(dp)  
print(dp[n][N] * 10)
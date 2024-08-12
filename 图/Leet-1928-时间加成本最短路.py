"""
一个国家有 n 个城市，城市编号为 0 到 n - 1 ，题目保证 所有城市 都由双向道路 连接在一起 。道路由二维整数数组 edges 表示，其中 edges[i] = [xi, yi, timei] 表示城市 xi 和 yi 之间有一条双向道路，耗费时间为 timei 分钟。两个城市之间可能会有多条耗费时间不同的道路，但是不会有道路两头连接着同一座城市。

每次经过一个城市时，你需要付通行费。通行费用一个长度为 n 且下标从 0 开始的整数数组 passingFees 表示，其中 passingFees[j] 是你经过城市 j 需要支付的费用。

一开始，你在城市 0 ，你想要在 maxTime 分钟以内 （包含 maxTime 分钟）到达城市 n - 1 。旅行的 费用 为你经过的所有城市 通行费之和 （包括 起点和终点城市的通行费）。

给你 maxTime，edges 和 passingFees ，请你返回完成旅行的 最小费用 ，如果无法在 maxTime 分钟以内完成旅行，请你返回 -1 。
"""

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # dp状态, dp[city][time]表示"刚好"时间为time时候到达city的最小花费
        # (1) dp[0][0]: 本地0的花费
        # (2) dp[city][time]只会依赖time更小的状态
        # (3) 相求的目标min(dp[n-1][*])
        n = len(passingFees)
        dp = [[inf for _ in range(maxTime + 1)] for _ in range(n) ]
        dp[0][0] = passingFees[0]
        # 遍历时间从小到大, time依赖time-1,...,0的结果

        for time in range(1, maxTime + 1):
            for A, B, dAB in edges:
                if time >= dAB:
                    dp[B][time] = min(dp[B][time], dp[A][time - dAB] + passingFees[B])
                    dp[A][time] = min(dp[A][time], dp[B][time - dAB] + passingFees[A])

        ans = min([dp[n - 1][time] for time in range(maxTime + 1)] )
        if ans == inf:
            return -1

        return ans




"""

Leet-188. 买卖股票的最佳时机 IV

给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""

class Solution:
     def maxProfit(self, k: int, prices: list[int]) -> int:
          n = len(prices)
          inf = float("inf")
          # dp[i][j]表示在第i天-第j次交易(卖算一次交易结束)后的[最大利润]
          # dp[i][j][0]: 表示i天结束, 手里没有股票
          # dp[i][j][1]: 表示i天结束, 手里还有股票 

          dp = [[[0, 0] for j in range(k + 1)] for i in range(n + 1)]
          # 使得第1天买入是合理的(- prices[i - 1])
          # 即第0天不能持有股票
          for j in range(k + 1):
               # dp[0][j][0] = 0 # dp = [[[-inf, -inf] for j in range(k + 1)] for i in range(n + 1)]
               dp[0][j][1] = -inf
     
          for i in range(1, n + 1):
               for j in range(1, k + 1):
                    # (1) i - 1天没有股票, i天也没有
                    # (2) i - 1天有股票,   i天卖了
                    dp[i][j][0] = max(dp[i - 1][j][0]
                                    , dp[i - 1][j][1] + prices[i - 1])
                    
                    # 如果全是0的话, 第一天直接不买了
                    # (1) i - 1天没有股票(触发买入, 用上一次交易j-1结果), i天买入
                    # (2) i - 1天有股票,   i天没卖
                    dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i - 1]
                                    , dp[i - 1][j][1]) # 第1天(dp[1]只能买不能转移)

          return max([dp[n][j][0] for j in range(k + 1)])


s = Solution()
k = 2
prices = [2,4,1]
print(s.maxProfit(k, prices))








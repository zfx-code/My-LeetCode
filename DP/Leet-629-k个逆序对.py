class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # 定义 f[i][j] 为考虑使用数值 [1,i]，凑成逆序对数量恰好为 j 的数组个数
        # 对第i个数所在的位置进行讨论, 共有i种选择(0, 1,..., i - 1)
        # 假设i在位置k上([0,...,i - 1]), 需要对这些情况sum
        # 则i与[k前的数无逆序对], 与[k之后的数全是逆序对]: (i - 1) - k 
        # 与i没关系(k前边)的逆序对数量是j-(i-1-k) = f[i - 1][j-(i-1-k)]

        # f[i][j] = sum(f[i - 1][j - (i - 1 - k)])_k=[0, i - 1]
        # n*k个状态, 总复杂度O(n^2*k), 10^9超时
        # sum(f[i - 1][j - (i - 1 - k)])_k=[0, i - 1]是上次f[i - 1][x]的某个前缀
        # 使用前缀和数组优化, 将计算单个状态复杂度从O(n)降到O(1)

        f = [[0 for j in range(k + 1)] for i in range(n + 1)]
        # 前缀
        s = [[0 for j in range(k + 1)] for i in range(n + 1)]
        f[1][0] = 1 
        for j in range(k + 1):
            s[1][j] = 1

        mod = 1000000000 + 7
        for i in range(2, n + 1):
            for j in range(k + 1):
                if j < i:
                    f[i][j] = s[i - 1][j] % mod
                else:
                    f[i][j] = (s[i - 1][j] - s[i - 1][j - (i - 1) - 1]) % mod
                # 前缀和数组
                if j == 0:
                    s[i][j] = f[i][j]
                else:
                    s[i][j] = (s[i][j - 1] + f[i][j]) % mod
        
        return int(f[n][k])



"""
134. 加油站

在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

示例 1:

输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:

输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。

"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # (1) 暴力, 遍历模拟每个起点
        n = len(gas)

        i = 0
        while i < n:
            remain = gas[i]
            j = i
            # 至少j -> j + 1是能走的
            while remain - cost[j] >= 0: 
                # 先走j, 再补j + 1
                remain = remain - cost[j] + gas[(j + 1) % n]
                j = (j + 1) % n

                # 回到了i点, 从i出发可行 
                if j == i:
                    return i
            # [0, i, n - 1] 0 <= i <= n - 1
            # (1) 0, i, j, n - 1
            # (2) j跨过边界, 0 < j < i, 0从[0, i]范围内已经被检查过了
            # 
            if j < i: 
                return -1
            # 从j -> j + 1(j != i - 1)失败了, 
            # 能到的点是j, 到不了j + 1)
            # (1) j > i(没跨边界)i + 1一直到j都不可能绕一整圈
            # 否则i + 1出发能到j + 1, 而i能到i + 1也能到j + 1与只能到j矛盾
            i = j + 1
            
        
        return -1
                





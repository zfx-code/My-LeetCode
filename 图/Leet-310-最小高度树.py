"""
Leet-310-最小高度树
树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，任何一个没有简单环路的连通图都是一棵树。

给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。

可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。

请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。

树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。

# 一些概念/定理
链：满足与任一结点相连的边不超过 2 条的树称为链

树的直径：树的直径，是指树上最长的一条链

树的中心：以树的中心为树的根时，树的高度最小

如何求树的直径和中心
(1) 2次DFS, 以any Node为root, 找到最深的叶节点A
    再以A为root找到最深叶节点B
    A->B为直径, 中心在A->B的中间位置(类似中位数, 1/2个)

该题思路可用拓扑排序实现
从叶节点开始delete节点, 每次把所有叶节点delete
下一次会出现新的叶节点, 重复直到剩下1/2个节点即为答案
时空双O(n)
"""

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        from queue import Queue
        q = Queue()

        # 入度
        in_degree = [0 for i in range(n)]
        # 邻接表
        table = [[] for i in range(n)]
        for u, v in edges:
            in_degree[u] += 1
            in_degree[v] += 1
            table[u].append(v)
            table[v].append(u)

        for i in range(n):
            # 叶子节点(入度为1)
            if in_degree[i] == 1:
                q.put(i)

        # 必须保证真正的root在队列里
        remainNode = n
        while remainNode > 2:
            size = q.qsize()
            for _ in range(size):
                remainNode -= 1
                u = q.get()
                for v in table[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 1:
                        q.put(v)

        # 最多剩2个
        ans = [q.get()]
        if not q.empty():
            ans.append(q.get())

        return ans

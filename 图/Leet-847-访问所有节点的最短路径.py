"""
847. 访问所有节点的最短路径

存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。

给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
"""

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # 状态压缩表示[当前点的访问状态], n_max = 12
        # a = (state >> x) & 1 (state中第x位是否被访问)
        # 添加访问标记 state | (1 << x)

        # 最大的状态表示(n个1再+1)
        mask = 1 << n

        # 初始化所有state的距离
        # 初始0, 结尾mask - 1(全经过一遍)
        dist = [[inf for _ in range(n)] for _ in range(mask)]

        from queue import Queue 
        q = Queue()
        # 以任一点作为起点出发, 距离为0 

        for i in range(n):
            # 从i出发, 状态为1 << i(只访问了i)的最短路程
            dist[1 << i][i] = 0
            # (state, u) 
            q.put([1 << i, i])


        while not q.empty():
            state, u = q.get()
            # 走的步数
            step = dist[state][u]

            if state == mask - 1:
                return step 
            
            # 可以走到v, 且更短
            for v in graph[u]:
                if dist[state | (1 << v)][v] == inf:
                    dist[state | (1 << v)][v] = step + 1 
                    q.put([state | (1 << v), v])
        
        return -1
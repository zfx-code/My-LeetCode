"""
你在一个城市里，城市由 n 个路口组成，路口编号为 0 到 n - 1 ，某些路口之间有 双向 道路。输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。

给你一个整数 n 和二维整数数组 roads ，其中 roads[i] = [ui, vi, timei] 表示在路口 ui 和 vi 之间有一条需要花费 timei 时间才能通过的道路。你想知道花费 最少时间 从路口 0 出发到达路口 n - 1 的方案数。

请返回花费 最少时间 到达目的地的 路径数目 。由于答案可能很大，将结果对 109 + 7 取余 后返回。
"""

# A -> B最短路径(边权重>0)
"""
简单起见, 先考虑无向图(双向均可走)
核心步骤
(1) 从未标记节点选择离出发点最近的节点A, 标记->加入最优路径
(2) 计算A临近节点B的距离, 若更小则更新B, 并更新B的prefix
"""
def Dijkstra_alg():
    INF = 0xffffffff
    n = 7
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

    # g[i][j]表示i到j的距离, INF表示无穷大
    g = [[INF for j in range(n)] for i in range(n)]
    for r in roads:
        g[r[0]][r[1]] = r[2]
        g[r[1]][r[0]] = r[2]
    
    # vis是否被访问过
    vis = [0 for i in range(n)]
    # 前缀节点 
    pre = [-1 for i in range(n)]
    pre[0] = 0
    # 距离出发点的距离
    dist = [INF for i in range(n)]
    dist[0] = 0
    # 每次加入一个
    for i in range(n):
        # (1) 选一个离出发点最近的A(dist[i]最小 and vis[i] == 0)
        A = -1
        for j in range(n):
            # 第一个直接拿进来(A=-1)
            if vis[j] == 0 and (A == -1 or dist[j] < dist[A]):
                A = j
        vis[A] = 1 

        # (2) 再找A的临近节点B
        for B in range(n):
            if B == A:
                continue 
            B_dist_new = dist[A] + g[A][B]
            if B_dist_new < dist[B]:
                dist[B] = B_dist_new 
                pre[B] = A

    print(pre)
    print(dist)
    return dist[-1]


# Dijkstra_alg()
# 基于优先队列实现Dijkstra, 方便(1)寻找离0点最近的点A
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # g[i][j]表示i到j的距离, INF表示无穷大
        g = [[inf for j in range(n)] for i in range(n)]
        # g[0][0] = 0
        # 使用邻接表
        neighbors = [[] for _ in range(n)]
        for u, v, d in roads:
            # g[u][v] = g[v][u] = d
            neighbors[u].append((v, d))
            neighbors[v].append((u, d))

        # vis是否被访问过
        vis = [0 for i in range(n)]
        # f表示最短路径数目
        f = [0 for i in range(n)]
        f[0] = 1
        # 距离出发点的距离
        dist = [inf for i in range(n)]
        dist[0] = 0
        MOD = 10**9 + 7

        from queue import PriorityQueue
        # 使用优先队列实现
        pq = PriorityQueue()
        # [0-i的最短距离, i编号]
        pq.put([0, 0])

        while not pq.empty():
            # 当前队列中离0点最近的[距离dA, 节点A]
            dA, A = pq.get()

            # 以A为起点搜索最短的
            for B, dAB in neighbors[A]:
                new_dist_B = dA + dAB
                if new_dist_B < dist[B]:
                    dist[B] = new_dist_B
                    # 方案数
                    f[B]    = f[A]
                    # 需要加入队列处理
                    pq.put([new_dist_B, B])
                elif new_dist_B == dist[B]:
                    # 多了一些路径
                    f[B] = (f[B] + f[A]) % MOD


        return f[-1]

# 权重<0 Bellman-Ford算法

# 任意两点最短路径 Floyd算法



"""
743. 网络延迟时间

有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 优先队列的Dijkstra算法
        # 起点为k, 不是0 
        # 以k为起点到各个点的最短时间
        # dist = [inf for i in range(n + 1)]
        # dist[k] = 0 
        
        # edges = [[] for i in range(n + 1)]
        # # 建图, 邻接表(有向图)
        # for u, v, w in times:
        #     edges[u].append([v, w])
        
        # from queue import PriorityQueue
        # pq = PriorityQueue()

        # # init(dA, A)
        # pq.put([0, k])
        # while not pq.empty():
        #     dA, A = pq.get()
        #     for B, dAB in edges[A]:
        #         new_dist_B = dA + dAB
        #         if new_dist_B < dist[B]:
        #             dist[B] = new_dist_B 
        #             pq.put([new_dist_B, B])
        # ans = max(dist[1:])
        # if ans == inf:
        #     return -1
        # return ans


        # Floyd算法(多源最短路)
        # 可以得到从任意起点出发, 到达任意点的最短距离
        edges = [[inf for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            edges[i][i] = 0 
        
        for u, v, w in times:
            edges[u][v] = w 
        
        # Floyd, 3层循环, (1) 中转点 (2) 起点 (3) 终点
        # 加上松弛操作(update)

        for p in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    edges[i][j] = min(edges[i][j], edges[i][p] + edges[p][j])
        
        ans = max(edges[k][1:])
        if ans == inf:
            return -1 
        
        return ans



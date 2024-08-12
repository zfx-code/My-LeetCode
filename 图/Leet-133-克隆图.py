"""
Leet-133-克隆图

给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}
 

测试用例格式：

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。

邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。
"""




# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
        
        if len(node.neighbors) == 0:
            return Node(node.val)
        
        # 有node, 有neighbors
        # 最多100个节点, 从1开始编号
        maxN = 101
        Nodes = [Node(i) for i in range(maxN)]
        # 记录是否访问过, 避免递归循环
        visited = [False for i in range(maxN)]
        
        # 队列做
        from queue import Queue
        q = Queue()
        q.put(node)
        

        while not q.empty():
            size = q.qsize()
            for _ in range(size):
                cur = q.get()
                if visited[cur.val]:
                    continue
                visited[cur.val] = True 
                # 添加neighbors
                neighbors = []
                for neighbor in cur.neighbors:
                    neighbors.append(Nodes[neighbor.val])
                    q.put(neighbor)
                Nodes[cur.val].neighbors = neighbors
                print(f"{cur.val} neighbors: {[a.val for a in neighbors]}")
        
        return Nodes[1]

        
Nodes = [Node(i) for i in range(5)]
Nodes[1].neighbors = [Nodes[2], Nodes[4]]
Nodes[2].neighbors = [Nodes[1], Nodes[3]]
Nodes[3].neighbors = [Nodes[2], Nodes[4]]
Nodes[4].neighbors = [Nodes[1], Nodes[3]]

s = Solution()

s.cloneGraph(Nodes[1])

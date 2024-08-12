"""
Leet-1483-树节点的第K个祖先

给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。

树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。

实现 TreeAncestor 类：

TreeAncestor（int n， int[] parent） 对树和父数组中的节点数初始化对象。
getKthAncestor(int node, int k) 返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。

"""

class TreeAncestor:
    """
    找node的第k个祖先, 向上找
        node -> parent[node] -> parent[parent[node]] -> ...
    需要跳k次才能到达node的第k个祖先, 时间复杂度为O(k)

    初步想法, 预处理出[爷爷节点](父节点的父节点), 可以2步2步的跳
    进一步预处理出[爷爷节点的爷爷节点], 可以4步4步的往上跳
    
    最终思路:
    预处理出每个节点的第2^i个祖先节点, 即1, 2, 4, 8,...
    eg: 13=8+4+1, 只要跳3步即可找到第13个祖先

    算法:
    TreeAncestor()构造函数中, 预处理出每个节点x的第2^i个祖先节点
    记作pa[x][i], 若2^i祖先节点不存在, 则pa[x][i] = -1
    (1) 先枚举i, 再枚举x(先算出所有爷爷节点, 再算出爷爷节点的爷爷节点)
    (2) pa[x][0] = parent[x], 父节点
    (3) pa[x][1] = pa[pa[x][0]][0], 爷爷节点
    (4) pa[x][i + 1] = pa[pa[x][i]][i], 表示x的2^i的2^i祖先是x的第2^{i+1}个祖先
        另外, 若pa[x][i] = -1, 则pa[x][i + 1] = -1
    (5) i + 1至多为log2(n)
    """
    def __init__(self, n: int, parent: list[int]):
        m = n.bit_length() - 1
        pa = [[p] + [-1] * m for p in parent]

        # 预处理2^i祖先节点
        for i in range(m):
            for x in range(n):
                p = pa[x][i]
                if p != -1:
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            # 二进制从低到高第i位是1
            if (k >> i) & 1:
                node = self.pa[node][i]
                if node < 0:
                    break 
        
        return node


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/solutions/2305895/mo-ban-jiang-jie-shu-shang-bei-zeng-suan-v3rw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
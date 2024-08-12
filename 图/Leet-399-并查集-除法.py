"""
399. 除法求值

给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
注意：x 是未定义的 => -1.0
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]

并查集:
思路把不同变量, 转化为一个变量(需要有edge)
路径压缩, 直接指向根节点

无向图连通性 考虑 并查集 
有向图依赖性 考虑 深度广度优先 拓扑排序
"""



def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # hash表存除法"a/b"和变量"a","b"
    # 还需要判断导出变量
    hashtable = dict()

    # 分子表A + 分母表B 
    A = dict()
    B = dict()

    # 最多20条"a/b", 最多40个变量
    for i in range(len(values)):
        v = values[i]
        a, b = equations[i]
        if a in A:
            A[a] += [a, b]
        else:
            A[a] = [a, b]

        if a in B:
            B[a] += [a, b]
        else:
            B[a] = [a, b]
        
        if b in B:
            B[b] += [a, b]
        else:
            B[b] = [a, b]
        
        if b in A:
            A[b] += [a, b]
        else:
            A[b] = [a, b]

        hashtable[f"{a}/{a}"] = 1.0
        hashtable[f"{b}/{b}"] = 1.0
        hashtable[f"{a}/{b}"] = v 
        hashtable[f"{b}/{a}"] = 1.0 / v 
    
    # 建
    # 导出条件是a分子=b分母或相反
    A_keys = list(A.keys())
    B_keys = list(B.keys())
    print(A_keys)
    print(B_keys)
    m = len(A_keys)
    n = len(B_keys)
    i, j = 0, 0 
    while i < m:
        a = A_keys[i]
        while j < n:
            b = B_keys[j]
            if a == b or f"{a}/{b}" in hashtable:
                continue 
            # 查找"a/b"是否可行, 看A[a]与B[b]是否有交集
            # eg: 有["a/c", "c/b"], 可导出"a/b"
            # 一旦更新, 直接跳到重新计算i=0
            flag = False
            for c in A[a]:
                if c in B[b]:
                    hashtable[f"{a}/{b}"] = hashtable[f"{a}/{c}"] * hashtable[f"{c}/{b}"]
                    hashtable[f"{b}/{a}"] = 1.0 / hashtable[f"{a}/{b}"]
                    flag = True 
                    break
            if flag:
                i = 0 
                j = 0
                break 

            j += 1 
        i += 0

    for key in hashtable:
        print(f"{key} = {hashtable[key]}")
    # 查
    ans = []
    for a, b in queries:
 
        if f"{a}/{b}" in hashtable:
            ans.append(hashtable[f"{a}/{b}"])
        else:
            ans.append(-1.0)
    
    return ans
    
equations =[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values =[3.0,4.0,5.0,6.0]
queries =[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
# print(calcEquation(equations=equations, values=values, queries=queries))



class UnionFind:

    def __init__(self):
        """
        记录每个节点的父节点, 与树相反
        若节点是相互连通的, 则他们在同一颗树里/他们的root相同
        """
        self.father = dict()
    
    # 初始化
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
    
    # 查找root + 路径压缩, 设置Tree-depth=2
    # 路径压缩复杂度是O(log^*(n)): 取多少次log2(n)向下去做变成1, ≈O(1)
    def find(self, x):
        root = x 
        while self.father[root] != None:
            root = self.father[root]
        
        # 全都挂载在root上
        # eg: root->a1->a2->a3
        # return root->[a1, a2, a3] 
        while x != root:
            original_father = self.father[x]
            self.father[x] = root 
            x = original_father 

        return root 
    
    # 合并节点
    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y 
    

    def is_union(self, x, y):
        return self.find(x) == self.find(y)

# 带权重的并查集模板
# 分子: 子节点
# 分母: 父节点
class UnionFind_weight:

    def __init__(self):
        """
        记录每个节点的父节点, 与树相反
        若节点是相互连通的, 则他们在同一颗树里/他们的root相同
        """
        self.father = dict()
        self.value = dict()
    
    # 初始化
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0
    
    # 查找root + 路径压缩, 设置Tree-depth=2
    # 路径压缩复杂度是O(log^*(n)): 取多少次log2(n)向下去做变成1, ≈O(1)
    def find(self, x):
        root = x 
        # 更新节点权重需要放大的倍数
        base = 1
        print(f"cur father: {self.father}")
        print(f"cur value: {self.value}")
        print(f"x: {x}")
        while self.father[root] != None:
            root = self.father[root]
            
            base *= self.value[root]
            print(f"->{root}, base={base}")
        
        print(f"x: {x}, root: {root}")
        print(f"x_val: {self.value[x]}, root_val: {self.value[root]}")
        print(f"base: {base}")
        # 全都挂载在root上
        while x != root:
            original_father = self.father[x]
            # 放大, 不包括自己原来的, 只用看上层
            self.value[x] *= base 
            base /= self.value[original_father]
            print(f"original_father: {original_father}, val: {self.value[original_father]}")
            ############
            self.father[x] = root 
            x = original_father 


        return root 
    
    # 合并节点
    def merge(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y 
            # 四边形法则(已知3条边, 计算两个root的关系)
            self.value[root_x] = self.value[y] * val / self.value[x]
    

    def is_union(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)

def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    uf = UnionFind_weight()
    for i in range(len(values)):
        a, b = equations[i]
        val = values[i]
        uf.add(a)
        uf.add(b)
        uf.merge(a, b, val)
        print("################")
        print(uf.father)
        print(uf.value)

    ans = []
    # for x in uf.father:
    #     uf.find(x)
    
    print("################")
    print(uf.father)
    print(uf.value)
    for a, b in queries:
        if uf.is_union(a, b):
            print(f"{a}: {uf.value[a] }, {b}: {uf.value[b] }")
            ans.append(uf.value[a] / uf.value[b])
        else:
            ans.append(-1.0)
    
    print(ans)
 
    return ans
    

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
"""
距离说明倍数怎么乘的
a/b=2, b/c=3
a->b(2)->c(3)
此时先找到a->b, base *= value["b"](注意不包含value["a"])
之后继续找b->c, base *= value["c"](1)
base = 3.0
随后a->c, 挂载的value["a"] *= base, 从2修正到2*3=6
base = base / value["b"] = 1
即a乘的base都是a.father一直到root的累计
不包括a->a.father, 这样达成a->root
随后同理, 重复a.father->root直到已经全部直接挂在root下
"""
calcEquation(equations, values, queries)



a = list(map(int, ["12", "34"]))

print(a)


from queue import PriorityQueue 

pq = PriorityQueue()

import heapq 
from collections import deque 

d = deque()


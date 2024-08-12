class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @param k int整型 
# @return TreeNode类
#
class Solution:
    def cyclicShiftTree(self , root: TreeNode, k: int) -> TreeNode:
        # write code here
        # 1. 层次遍历 + 分层
        from queue import Queue 
        q = Queue()
        q.put(root)

        level_nodes = []
        # 记录father, "left" or "right"
        father = dict()
        while q.empty() == False:
            nodes = []
            # 这一层有多少个
            level_n = q.qsize()
            idx = 0
            for i in range(level_n):
                node = q.get()
                nodes.append(node)
                
                if node.left:
                    father[node.left.val] = idx
                    q.put(node.left)
         
                if node.right:
                    father[node.right.val] = idx + 1         
                    q.put(node.right)
                idx += 2
            level_nodes.append(nodes)
        
        # 2. 从最后一层做到第二层
        print(len(level_nodes))
        for i in range(len(level_nodes) - 1, 0, -1):
            # 上一层的节点, n_last, 可以有2 * n_last位置
            father_nodes = level_nodes[i - 1]
  
            child_idxs_new = [(father[node.val] + k) % (2 * len(father_nodes)) for node in level_nodes[i]]
            # print(f"old idx: {[father[node.val] for node in level_nodes[i]]}")
            # print(f"new idx: {child_idxs_new}")
            # 先清除所有的child
            for node in father_nodes:
                node.left = None 
                node.right = None 

            # 复原这些child的new father
            for j in range(len(child_idxs_new)):
                # child = level_nodes[i][j]
                idx = child_idxs_new[j] // 2 
                # left_or_right
                if child_idxs_new[j] % 2  == 0:
                    father_nodes[idx].left = level_nodes[i][j]
                else:
                    father_nodes[idx].right = level_nodes[i][j]

left = TreeNode(2)
right = TreeNode(3, TreeNode(4), TreeNode(5))
root = TreeNode(x=1
            , left=left
            , right=right
            )

s = Solution()

s.cyclicShiftTree(root=root, k=1)









def level_order(root):
    # write code here
    # 1. 层次遍历 + 分层
    from queue import Queue 

    q = Queue()

    q.put(root)

    level_nodes = []
    # 记录father, "left" or "right"
    father = dict()
    while q.empty() == False:
        nodes = []
        # 这一层有多少个
        level_n = q.qsize()
        idx = 0
        for i in range(level_n):
            node = q.get()
            nodes.append(node)
            
            if node.left:
                father[node.left.val] = idx
                q.put(node.left)
        
            if node.right:
                father[node.right.val] = idx + 1         
                q.put(node.right)
            idx += 2
        print([node.val for node in nodes])
        level_nodes.append(nodes)

level_order(root)





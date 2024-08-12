# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # 中序遍历结果
        self.inorder = dict()
        self.idx = 0

    # 改一下写法, 使用hash表而不是数组, 减少查询时间
    def in_order(self, root):
        if root == None:
            return 
        self.in_order(root.left)
        self.inorder[root] = self.idx
        self.idx += 1
        self.in_order(root.right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        需要一个判断节点在哪个子树的函数

        1. 不在同一个子树上, 公共祖先必须是root
        2. 在同一个子树上, return 递归(一半子树)

        特殊条件, 节点之一就是root
        root in [p, q], return root
        """
        if root in [p, q]:
            return root

        if root not in self.inorder:
            self.in_order(root)

        root_idx = self.inorder[root]
        p_idx = self.inorder[p]
        q_idx = self.inorder[q]
   
        # 在同一边: 左
        if p_idx < root_idx and q_idx < root_idx:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_idx > root_idx and q_idx > root_idx: 
            return self.lowestCommonAncestor(root.right, p, q)
        # 不在同一边
        else:
            return root
        

        # 判断即可
        def dfs(root, p, q):
            if root in [None, p, q]:
                return root 
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            # root的左右子树各有一个p, q则root就是最近的公共祖先
            if not left is None and not right is None:
                return root  
            
            # right is None, p, q in left 
            if not left is None:
                return left 
            
            if not right is None:
                return right 
            
            # 都没找到(p, q)
            return None 
        
        return dfs(root, p, q)
        

s = Solution()
child0 = TreeNode(4)
child1 = TreeNode(2, TreeNode(7), child0)
left = TreeNode(5, TreeNode(6), child1)
right = TreeNode(1)
root = TreeNode(x=3
            , left=left
            , right=right
            )

ans = s.lowestCommonAncestor(root, left, child0)
print(ans.val)

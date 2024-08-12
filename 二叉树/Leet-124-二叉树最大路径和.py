"""
124. 二叉树中的最大路径和

二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        思路:
        对于每一个node, 若不包含自己, 可以得到max(L, R)
        若包含自己, 需要得到同时包含node.left, node.right的路径和最大值
        
        # 返回[经过root]的单边分支的最大值, 可供给root的父节点使用
        dfs(root)
        
        """
        ans = -1000
        def dfs(root):
            nonlocal ans
            if not root:
                return 0 
            
            left_max  = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))

            # 结合left -> root -> right双路径的最大值
            ans = max(ans, root.val + left_max + right_max)

            # 尝试往上走, 结合root.father找到和更大的路径
            # 返回结合了当前root的单路最大
            return root.val + max(left_max, right_max)
        
        dfs(root)

        return ans 
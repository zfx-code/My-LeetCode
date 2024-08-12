"""
Leet-437-路径总和III

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        import collections
        # prefix[node] = sum(from [root] to [node])
        # 即使默认所有{key : 0}
        prefix = collections.defaultdict(int)
        prefix[0] = 1 

        ans = 0
        # 前缀和测试
        # curSum是不包含root的curSum
        def dfs(root, curSum):
            nonlocal ans, prefix
            if root is None:
                return 0
            
            curSum += root.val
            ans += prefix[ curSum - targetSum]

            # 将当前节点纳入更新(保证该节点之后的节点可以用到该结果)
            prefix[curSum] += 1
        
            # 进入左右子树
            dfs(root.left, curSum)
            dfs(root.right, curSum)

            # 释放当前节点(删除), 不再有以该节点向下的路径了
            prefix[curSum] -= 1

        dfs(root, 0)
        return ans

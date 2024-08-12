"""
Leet-96-不同的二叉搜索树

给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数

"""

class Solution:
    def numTrees(self, n: int) -> int:
        """
        n个节点存在二叉搜索树的个数是G(n)
        f(i)为以i为根的二叉搜索树个数
            G(n) = f(1)+...+f(n)
        当i为根节点时, 左子树节点个数是i-1, 右子树节点个数为n-i
            f(i)=G(i-1)*G(n-i)
        则卡特兰数公式:
            G(n)=G(0)*G(n-1)+G(1)*G(n-2)+...+G(n-1)*G(0)
        """
        # dp[i] += dp[j-1] * dp[i - j]

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1 

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]
    

"""
Leet-95-不同的二叉搜索树 II
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        # 对于[start, end]范围内的所有可行二叉搜索树
        # 考虑枚举值i作为root
        def dfs(start, end):
            if start > end:
                return [None]
            
            trees = []
            for i in range(start, end + 1):
                lefts = dfs(start, i - 1)
                rights = dfs(i + 1, end)

                # 拼起来
                for left in lefts:
                    for right in rights:
                        trees.append(TreeNode(i, left, right))

            return trees 
        
        return dfs(1, n)


from heapq import heapify
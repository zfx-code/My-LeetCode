"""
Leet-108-将有序数组转换为二叉搜索树
给你一个整数数组 nums ，其中元素已经按 [升序] 排列，
请你将其转换为一棵 [平衡] 二叉搜索树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        """
        二叉搜索树
        左子树都小, 右子树都大

        要求:"平衡"
        选择中间元素作为根节点
        """
        n = len(nums)
        # 根据中序建立平衡二叉搜索树
        # [low, high]
        def dfs(nums, low, high):
            if low > high:
                return 
            if low == high:
                return TreeNode(nums[low])

            # [low, mid - 1], mid, [mid + 1, high]
            mid = low + ((high - low) >> 1)

            root = TreeNode(nums[mid])
            root.left = dfs(nums, low, mid - 1)
            root.right = dfs(nums, mid + 1, high)

            return root
        return dfs(nums, 0, n - 1)
    
import collections

prefix = collections.defaultdict(int)


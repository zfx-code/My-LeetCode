"""
109. 有序链表转换二叉搜索树
给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为 
平衡二叉搜索树

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 从根到叶用递归，从叶到根用分治，这道题有中序排列了，所以用分治更好。
        return
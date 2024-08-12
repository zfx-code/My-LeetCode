"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
eg: 1->2->3->4->5->6
     1
  2     5
3   4      6
"""

# 前序

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order(root: TreeNode):
    if root == None:
        return 
    
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)

def flatten(self, root: TreeNode) -> None:
        def pre_order(root, res):
            if root == None:
                return None 
            res.append(root)
            pre_order(root.left, res)
            pre_order(root.right, res)
            
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        pre_order(root, nodes)
        
        if len(nodes) == 0:
            return 
            
        for i in range(len(nodes) - 1):
            nodes[i].left = None 
            nodes[i].right = nodes[i+1] 
        
        nodes[-1].left = None
        nodes[-1].right = None 

"""

只用O(1)空间
重复下过程
(1) tmp = cur.right, cur.right = cur.left, cur.left = None()
(2) tmp接到left的前序遍历最后一个节点
"""
def flatten_O1(root: TreeNode):
    #  返回前序的最后一个节点, 就是找右侧, 直到cur.right == None
    # 顺序是root, left, right
    # def pre_order_last(root):
    #     if root.right:
    #         return pre_order_last(root.right)
    #     elif root.left:
    #         return pre_order_last(root.left)
    #     else:
    #         return root
    
    # if root == None:
    #         return 
    
    cur = root 

    while cur.left or cur.right:
        if cur.left:
            # 拉直左边
            tmp = cur.right 
            cur.right = cur.left 
            cur.left = None 
            # 右边接到左边
            # last = pre_order_last(cur.right) 
            # 找最右节点
            last = cur.right 
            while last.right:
                last = last.right 
            last.right = tmp 
            print(f"last val: {last.val}")
            pre_order(root)
        # 处理完左边已经空了, 走到右边
        cur = cur.right
    

     

left = TreeNode(val=2, left=TreeNode(3), right=TreeNode(4))
right = TreeNode(val=5, left=None, right=TreeNode(6))
root = TreeNode(val=1, left=left, right=right)    

flatten_O1(root)

pre_order(root)

from collections import deque 
a = deque()

# deque.

# 右视图, 层次遍历变体, 只看右边
def rightSideView(root: TreeNode):
        if root == None:
            return [] 
        from collections import deque 

        q = deque([root])
        ans = []
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                if i == 0:
                    ans.append(cur.val)
            
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        
        return ans

# dfs思路
"""
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None: return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans
"""
"""
116. 填充每个节点的下一个右侧节点指针

给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

参考
https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solutions/100099/dong-hua-yan-shi-san-chong-shi-xian-116-tian-chong/
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(root):
            if root is None:
                return 
            
            left = root.left 
            right = root.right 

            while left:
                left.next = right
                # 关键左->右, 右->左 
                # 依次完成同一个father, 不同father的next连接
                left = left.right 
                right = right.left 
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return root
        
"""
complete binary tree

给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2^h 个节点。

进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？

################
2. 根据完全二叉树的性质简化遍历次数
这是一棵完全二叉树：除最后一层外，其余层全部铺满；且最后一层向左停靠

(1) 如果根节点的左子树深度等于右子树深度，则说明 左子树为满二叉树

(2) 如果根节点的左子树深度大于右子树深度，则说明 右子树为满二叉树

如果知道子树是满二叉树，那么就可以轻松得到该子树的节点数目：(1<<depth) - 1; // depth为子树的深度；为了加快幂的运算速度，可以使用移位操作符
接着我们只需要接着对另一子树递归即可
时间复杂度为 O(logn∗logn)O(logn * logn)O(logn∗logn)，空间复杂度为 O(1)O(1)O(1)【不考虑递归调用栈

作者：左
链接：https://leetcode.cn/problems/count-complete-tree-nodes/solutions/181466/c-san-chong-fang-fa-jie-jue-wan-quan-er-cha-shu-de/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 边界判断
        if root == None:
            return 0
        # 优化版本, 因为是完全二叉树
        # 最后一层之前都是满的
        # 获取子树深度-完全二叉树
        def get_Depth(root):
            depth = 0
            # 沿着左边走, 一定能走到最深
            while root:
                depth += 1
                root = root.left
            
            return depth
        
        depth_left = get_Depth(root.left)
        depth_right = get_Depth(root.right)

        # 左子树是满的, 继续看右子树
        if depth_left == depth_right:
            # 左子树 + 根节点 = 2^d, 再额外考虑右子树
            # else同理
            return (1 << depth_left) + self.countNodes(root.right)
        # 右子树是满的(比左子树低一层)
        else:
            return (1 << depth_right) + self.countNodes(root.left)

    



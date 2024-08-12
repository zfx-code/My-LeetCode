# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
遍历:
前序, 中序, 后序, 层次
关键就是看root node
前序: root->(left)->(right)
中序: (left)->root->(right)
后序: (left)->(right)->root

已知中+前/后可唯一确定一颗二叉树
已知前+后则不行
"""
# 前序
def pre_order(root: TreeNode):
    if root == None:
        return 
    
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)

# 中序
def in_order(root: TreeNode):
    if root == None:
        return 
    
    in_order(root.left)
    print(root.val)
    in_order(root.right)

# 后序
def post_order(root: TreeNode):
    if root == None:
        return 
    
    post_order(root.left)
    post_order(root.right)
    print(root.val)

#       1
#   2      3
# 4  5   6  7
left = TreeNode(val=2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(val=3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(val=1, left=left, right=right)

# print("preorder:")
# pre_order(root)
# print("inorder:")
# in_order(root)
# print("postorder:")
# post_order(root)

# 从前序+中序遍历建树
def buildTree_pre_in(preorder: list[int], inorder: list[int]) -> TreeNode:
    if len(preorder) == 0:
        return None
    
    # if len(preorder) == 1:
    #     return TreeNode(preorder[0])
    
    # print("preorder:")
    # print(preorder)
  
    # print("inorder:")
    # print(inorder)
    # 找根节点
    root = TreeNode(preorder[0])
    # 中序遍历的左是左子树, 右是右子树
    # 使用哈希表加快索引
    root_idx = inorder.index(root.val)

    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx+1:]

    left_preorder = preorder[1:1+len(left_inorder)]
    right_preorder = preorder[1+len(left_inorder):1+len(left_inorder)+len(right_inorder)]

    root.left = buildTree_pre_in(left_preorder, left_inorder) 
    root.right = buildTree_pre_in(right_preorder, right_inorder)

    return root 

# 从中序+后序遍历建树
def buildTree_in_post(inorder: list[int], postorder: list[int]) -> TreeNode:
    if len(postorder) == 0:
        return None
    
    print(postorder)
    print(inorder)
    # 找根节点
    root = TreeNode(postorder[-1])
    # 中序遍历的左是左子树, 右是右子树
    # 使用哈希表加快索引
    root_idx = inorder.index(root.val)

    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx+1:]

    left_postorder = postorder[:len(left_inorder)]
    right_postorder = postorder[len(left_inorder):len(left_inorder)+len(right_inorder)]

    root.left = buildTree_in_post(left_inorder, left_postorder) 
    root.right = buildTree_in_post(right_inorder, right_postorder)

    return root 

# preorder = [1,2]
# inorder = [2,1]
# hashtable = dict()
# for i in range(len(inorder)):
#     hashtable[inorder[i]] = i

# # root = buildTree(preorder=preorder, inorder=inorder)

# # pre_order(root)
# # in_order(root)

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]

# root = buildTree_pre_in(inorder=inorder, postorder=postorder)

# in_order(root)


# 层次遍历 + 层次输出
# 确定共k个层级, 每个层级多少元素
def level_order(root):
    from queue import Queue
    q = Queue()

    q.put(root)
    level = []
    while q.empty() == False:
        # 这n个位于1个level
        n = q.qsize()
        tmp = []
        for _ in range(n):
            head = q.get()
            tmp.append(head.val)
            if head.left:
                q.put(head.left)
            if head.right:
                q.put(head.right)
            # print(head.val)
        level.append(tmp)
    print(level)    

    return level
#       1
#   2      3
# 4  5   6  7
left = TreeNode(val=2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(val=3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(val=1, left=left, right=right)
level_order(root)


def test(a: 'TreeNode'):
    print(a.val)

test(root)
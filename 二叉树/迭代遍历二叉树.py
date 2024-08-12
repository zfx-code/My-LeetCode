# 作者这个思路得到后序遍历的非递归是没有问题的。但是有时候二叉树的非递归我们不仅仅是为了解决遍历问题，例如后序遍历堆栈里保存的始终是该节点的祖先节点这一性质可以用于解决寻找公共祖先的问题。遇到这种问题作者的这种反转先序遍历的思路就不行了。所以最好还是可以快速写出常规的非递归遍历比较好。懒得写题解了，借作者宝地写一个本人写的三种非递归的统一模板式写法。 二叉树的非递归难点其实就在于后序遍历，因为后序需要两次路过根节点。遍历的时候需要根据第几次路过来决定是否访问根节点。解决的办法是增加一个r指针，指向上次访问的节点。因为后序遍历LRN最后一定是遍历根节点，所以当r指向root.right的时候那么就是该遍历root的时候了。

public void LRN(TreeNode root) {
    LinkedList<TreeNode> s = new LinkedList<>();
    TreeNode t = root;
    TreeNode r = null; //记录上次访问过的节点
    //当t指针为空，而且堆栈也为空的时候遍历就结束了
    while (t!=null || !s.isEmpty()){
        //每次当t不为空的时候就默认把t压入堆栈
        if (t!=null){
            s.addFirst(t);
            t = t.left;
        } else {
            t = s.getFirst();
            if (t.right!=null && r != t.right){
                //该节点的右孩子不空，而且上一个访问的不是右孩子(证明这是从左孩子回溯过来的)
                t = t.right;
            } else {
                //该节点的右孩子为空，或者右孩子已经访问过了
                t = s.removeFirst();
                System.out.println(t);  //遍历节点
                r = t;
                t = null; //防止t被压入堆栈，所以要置空
            }
        }
    }
}
# 遍历(print)就看第几次访问
public void NLR(TreeNode root) {
    LinkedList<TreeNode> s = new LinkedList<>();
    TreeNode t = root;
    //当t指针为空，而且堆栈也为空的时候遍历就结束了
    while (t!=null || !s.isEmpty()){
        //每次当t不为空的时候就默认把t压入堆栈
        if (t!=null){
            System.out.println(t); //遍历节点
            s.addFirst(t);
            t = t.left;
        } else {
            t = s.removeFirst();
            t = t.right;
        }
    }
}

public void LNR(TreeNode root) {
    LinkedList<TreeNode> s = new LinkedList<>();
    TreeNode t = root;
    //当t指针为空，而且堆栈也为空的时候遍历就结束了
    while (t!=null || !s.isEmpty()){
        //每次当t不为空的时候就默认把t压入堆栈
        if (t!=null){
            s.addFirst(t);
            t = t.left;
        } else {
            t = s.removeFirst();
            System.out.println(t); //遍历节点
            t = t.right;
        }
    }
}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 后序遍历
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        t = root 
        # 记录上次访问过的节点
        r = None 
        ans = []
        while t or len(stack) > 0:
            # t不空则入栈
            if t:
                stack.append(t)
                t = t.left 
            else: 
                t = stack[-1]
                # 该节点有右孩子, 且上一次访问的不是右孩子(from 左孩子)
                if t.right and r != t.right:
                    t = t.right
                # 没有右孩子, 或已经访问过了(回到了根节点, 该往上走了)
                else:
                    t = stack.pop()
                    ans.append(t.val)
                    r = t 
                    t = None 
        
        return ans
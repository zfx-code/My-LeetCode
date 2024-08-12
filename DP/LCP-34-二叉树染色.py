
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:
        
        # colored代表当前root是否染色
        # 若染色, 则额外约束, 与该节点相连的节点最多染k个
        def dfs(root, colored, k):
        
            if not root or k == 0:
                return 0

            # 变成左子树最大 + 右子树最大(体现了只跟当前节点有关)
            # 左右都可以最长k个
            if colored == 0:
                l1 = dfs(root.left, 0, k)
                l2 = dfs(root.left, 1, k)
                r1 = dfs(root.right, 0, k)
                r2 = dfs(root.right, 1, k)
                return max(l1, l2) + max(r1, r2)
            
            ans = 0
            # 根节点染色, 则左+右<=k-1
            for i in range(k):
                for j in range(k - i):
                    if i == 0 and j == 0:
                        left = dfs(root.left, 0, k)
                        right = dfs(root.right, 0, k)
                        ans = max(ans, left + right)
                    elif i == 0 and j > 0:
                        left = dfs(root.left, 0, k)
                        right = dfs(root.right, 1, j)
                        ans = max(ans, left + right)
                    elif i > 0 and j == 0:
                        left = dfs(root.left, 1, i)
                        right = dfs(root.right, 0, k)
                        ans = max(ans, left + right)
                    else:
                        left = dfs(root.left, 1, i)
                        right = dfs(root.right, 1, j)
                        ans = max(ans, left + right)

            return ans + root.val

        return max(dfs(root, 0, k), dfs(root, 1, k))

        # colored代表当前root是否染色
        # 若染色, 则额外约束, 与该节点相连的节点最多染k个
        # dp返回一个数组
        # 里边包含, 以当前root开始, 遍历左右子树的染色最大值
        def dp(root, k):
            if not root:
                return [0] * (k + 1)

            left_arr = dp(root.left, k)
            right_arr = dp(root.right, k)
            
            arr = [0] * (k + 1)
            # arr[0]表示root不染色
            arr[0] = max(left_arr) + max(right_arr)

            # arr[i]表示root染色, 并最长连续染色i个
            # arr[1]表示root染色, 且左右不能染色
            arr[1] = root.val + left_arr[0] + right_arr[0]

            # i >= 2 
            for i in range(2, k + 1):
                # 左边j, 最多染i - 1个(因为root已经确定染色了)
                # 右边i - 1 - j
                for j in range(i):
                    arr[i] = max(arr[i], left_arr[j] + right_arr[i - 1 - j])
                # 放前边可能会丢掉 < root.val的值
                arr[i] += root.val
            return arr
        
        return max(dp(root, k))
        
root= TreeNode(5)
left = TreeNode(2)
left.left = TreeNode(4) 
right = TreeNode(3)
root.left = left 
root.right = right 

k = 2

s = Solution()
print(s.maxValue(root, 2))


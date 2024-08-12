"""
排列组合专场

46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]

"""
class Solution:
    # 全排列, A(n, n), [1, 2]与[2, 1]不同
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        visited = [False] * n 
        ans = []

        def dfs(cur):
            nonlocal ans, visited
            if len(cur) == n:
                ans.append(cur)
                return  

            # 继续尝试添加
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    dfs(cur + [nums[i]])
                    visited[i] = False 

        dfs([])
        return ans                

    # 组合C(n, k) [1, 2]与[2, 1]相同
    # 注意: 是1-n, 而不是0-n-1
    # 加入剪枝优化
    def combine(self, n: int, k: int) -> list[list[int]]:
        visited = [False] * (n + 1) 
        ans = []

        def dfs(cur):
            nonlocal ans, visited
            if len(cur) == k:
                ans.append(cur)
                return  

            start = 1 
            if len(cur) > 0:
                start = cur[-1] + 1
            # 剪枝
            if len(cur) + (n + 1 - start) < k:
                return
            # 继续尝试添加, 不过只考虑大的数, 小的之前做过了
            for i in range(start, n + 1):
                if not visited[i]:
                    visited[i] = True
                    dfs(cur + [i])
                    visited[i] = False 

        dfs([])
        return ans     

    # 回溯
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        # 排序
        candidates.sort()

        ans = []

        # start表示当前可以加的数的索引
        # 不能回头, 下一次加start + 1位置的数
        def dfs(cur, start):
            # print(f"cur: {cur}")
            nonlocal ans
            if sum(cur) == target:
                ans.append(cur)
                return 
            # 剪枝, 无法再加别的数
            if start > n - 1 or sum(cur) + candidates[start] > target:
                return 

            # 避免重复, 把1个数加到极限再说
            # eg: [2, 2, 3], 不要再考虑[2, 3, 2]
            # 不超过
            for j in range(1 + (target - sum(cur)) // candidates[start]):
                dfs(cur + [candidates[start]] * j, start + 1)

        dfs([], 0)
        return ans    
                   

s = Solution()
candidates = [2,3,6,7]
target = 7

print(s.combinationSum(candidates, target))
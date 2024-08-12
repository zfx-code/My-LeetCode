"""
40. 组合总和 II

给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]

"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        
        ans = []
        # cur: [a, b,...]
        # start: 下一步可选的位置
        def dfs(cur, cur_val, start):
            nonlocal ans
            if cur_val == target:
                ans.append(cur)
                return 
            
            # if start >= n or cur_val + candidates[start] > target:
            #     return  

            # 继续寻找别的解, 可以加不止一个
            for i in range(start, n): 
                if cur_val + candidates[i] > target:
                    return  
                # eg: [1,1,2], target=3
                # 避免出现[1,2],[1,2]这样的情况
                # 且允许选择[1,1,...]这样
                # 原理: 在当前选择下走到第二个"1"的时候表示第一个"1"没选(对应history走过的情况)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                dfs(cur + [candidates[i]], cur_val + candidates[i], i + 1)
        
        dfs([], 0, 0)

        return ans
    
"""
39. 组合总和

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

 

示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
"""

class Solution:
    # 回溯
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
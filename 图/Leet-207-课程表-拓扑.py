"""
207. 课程表
中等

你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

拓扑排序核心内容:
每次选择入度为0的点u, 删除该点u及其出边

可以使用拓扑排序判断图中是否存在环
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import deque
        # 先建图, edge[i]表示课程i的后续课
        edges = [[] for _ in range(numCourses)]

        # 入度
        inDegrees = [0] * numCourses
        # pre是cur的先修课程
        for cur, pre in prerequisites:
            inDegrees[cur] += 1
            edges[pre].append(cur)
  
        q = deque()   
        # 先把入度为0的点全拿出来
        for i in range(numCourses):
            if inDegrees[i] == 0:
                q.append(i)

        # 持续找入度为0的点
        while len(q) > 0:
            pre = q.popleft()
            numCourses -= 1
            for cur in edges[pre]:
                inDegrees[cur] -= 1
                if inDegrees[cur] == 0:
                    q.append(cur)
        
        return numCourses == 0


numCourses = 2
prerequisites = [[1,0]]

s = Solution()

print(s.canFinish(numCourses, prerequisites))




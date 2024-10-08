"""

630. 课程表 III

这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。

你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。

返回你最多可以修读的课程数目。

 

示例 1：

输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出：3
解释：
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
示例 2：

输入：courses = [[1,2]]
输出：1
示例 3：

输入：courses = [[3,2],[4,3]]
输出：0

"""

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        from heapq import heappush, heappop
        """
        贪心+反悔+优先队列

        DDL越早, 应该越早上完, 但可能duration比较长, 够别的上好几门

        按照lastDay从小到大排序, 然后选尽可能小的duration课来上
        """
        # 按照lastDay从小到大排序
        courses.sort(key=lambda x: x[1])

        h = []
        # 已经消耗的时间
        day = 0

        for duration, last_day in courses:
            if day + duration <= last_day:
                day += duration
                # 使用最大堆
                heappush(h, -duration)
            # 有个更短时间的课程
            elif h and duration < -h[0]:
                # 撤销之前duration最长的课, 修改为该课
                pre = - heappop(h)
                heappush(h, -duration)
                day = day - pre + duration
        
        return len(h)

from queue import PriorityQueue

pq = PriorityQueue()


"""
480. 滑动窗口中位数

中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
 """

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 难点在于懒删除，核心是要维护堆顶数据有效
        # 一般懒堆是用一个哈希表记录堆内的值，如果堆的当前状态跟哈希表记录的当前状态不一致说明当前元素是无效的

        # 大根堆维护小的部分
        small = []
        # 小根堆维护大的部分
        big = []

        # 维护哪些数据要出去
        mp = defaultdict(int)

        def getMedian(k):
            # 去除不在堆中的元素
            while len(small) > 0 and mp[-small[0]] > 0:
                mp[-small[0]] -= 1
                heapq.heappop(small)
            
            while len(big) > 0 and mp[big[0]] > 0:
                mp[big[0]] -= 1 
                heapq.heappop(big)
            
            if k % 2 == 1:
                return -small[0]
            return (-small[0] + big[0]) * 0.5
        
        def keepBalance(toSmall, x):
            if toSmall:
                heapq.heappush(big, x)
                heapq.heappush(small, -big[0])
                heapq.heappop(big)
            else:
                heapq.heappush(small, -x)
                heapq.heappush(big, -small[0])
                heapq.heappop(small)
        
        # 初始化k项 
        for i in range(k):
            # 保证在奇数情况下small.size()==big.size()+1，
            # 偶数情况下small.size()==big.size()
            if len(small) == len(big):
                keepBalance(True, nums[i])
            else:
                keepBalance(False, nums[i])
            
        ans = [getMedian(k)]
        for i in range(k, len(nums)):
            # 移除的
            left = nums[i - k]
            mp[left] += 1 
            # 如果要删除的元素在small堆中，则要把small堆大小加一
            if left <= -small[0]:
                keepBalance(True, nums[i])
            else:
                # 否则big堆大小加一
                keepBalance(False, nums[i])
            ans.append(getMedian(k))
        
        return ans
            



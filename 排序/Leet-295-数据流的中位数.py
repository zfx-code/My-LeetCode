"""
295. 数据流的中位数

中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
"""
import heapq
class MedianFinder:

    def __init__(self):
        # N = m(前一半, 大根堆) + n(后一半, 小根堆)
        # 保持m >= n, 最多多1, m = n +1
        self.before = []
        self.after  = []


    def addNum(self, num: int) -> None:
        
        # 规定, 若是奇数个, 则将中位数保存至前半段
        # (1) n, n (2) n + 1, n
        m = len(self.before)
        n = len(self.after)
        # m -> m + 1, 但是不直接插入, 而是先给after, 
        # 再返回给before确实是最小的
        if m == n:
            heapq.heappush(self.after, num)
            mid = heapq.heappop(self.after)
            heapq.heappush(self.before, -mid)
        # m > n, n补上
        else:
            heapq.heappush(self.before, -num)
            mid = -heapq.heappop(self.before)
            heapq.heappush(self.after, mid)

    def findMedian(self) -> float:
        m = len(self.before)
        n = len(self.after)
        if m == n:
            return 0.5 * (-self.before[0] + self.after[0])
        else:
            return -self.before[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

# 参考直接用写好的堆
# 堆排序后是按照从小到大排, 因此排-num结果是从大到小
# 最后pop出k-1个, 再pop最后一个, 取相反数即可
def findKthLargest(nums: List[int], k: int) -> int:
    pq = []
    for num in nums:
        heapq.heappush(pq, -num)
    for i in range(k - 1):
        heapq.heappop(pq)
    return -heapq.heappop(pq)


归并

桶排序

快排

堆排序, 优先队列
"大", "小"是形容root node的
建立大根堆 -> 对应升序排列(root node最大, 最先出来, 反而排最后)
建立小根堆 -> 对应降序排列
(1) 建堆
(2) 调整 
(3) 删除

注意heapq实现的是[小根堆], root是最小的
因此可以直接用于实现["第" or "前"] k小的
像实现k大则需要push进去-x, 取出的时候就是实际上大的结果了

下文代码实现的是[大根堆], root是最大的
直接可以实现["第" or "前"] k大的
"""
import heapq 

# 最大堆调整
def Max_Heapify(arr: list[int], i: int, heapSize: int):
    # i是父节点(最大), 两个child是[2i+1, 2i+2]
    left = 2 * i + 1 
    right = 2 * i + 2 
    largest = i 
    # 调整left
    if left < heapSize and arr[left] > arr[largest]:
        largest = left 
    
    if right < heapSize and arr[right] > arr[largest]:
        largest = right 
    
    # 真正的最大元素放到目标-i上
    if largest != i:
        # swap(arr[i], arr[largest])
        arr[i], arr[largest] = arr[largest], arr[i]
        # 重复这个过程, 现在largest可能不是(他的子树中)最大了
        Max_Heapify(arr, largest, heapSize)
    

# 建立最大堆
def build_Max_Heap(arr: list[int], heapSize: int):
    for i in range(heapSize // 2, -1, -1):
        Max_Heapify(arr, i, heapSize)

# 找第k大
def find_Kth_Largest(arr: list[int], k: int):
    heapSize = len(arr) 
    build_Max_Heap(arr, heapSize)

    # 每次交换(root, last), 然后重新调整堆
    # 出去了k - 1个root(依次最大), 剩下就是第k大的
    for i in range(len(arr) - 1, len(arr) - k, -1):
        # swap(arr[0], arr[i])
        arr[0], arr[i] = arr[i], arr[0]
        # 此时arr[i]是当前最大的, 然后扔掉
        heapSize -= 1
        # 调整的是root位置
        Max_Heapify(arr, 0, heapSize)

    return arr[0]

n = 5
arr = [1, 2, 3, 4, 5]
# build_Max_Heap(arr, n)
print(find_Kth_Largest(arr, 1))
print(arr)



pq = [-1,-2,-3,-4]
heapq.heappush(pq, -5)
# heapq.heappush(pq, 2)
# heapq.heappush(pq, [1, 2])
print(pq)

n = len(pq)

"""

295. 数据流的中位数

中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

双堆实现
"""

class MedianFinder:

    def __init__(self):
        # N = m(前一半, 大根堆) + n(后一半, 小根堆)
        # 保持m >= n, 最多多1, m = n +1
        self.before = []
        self.after  = []


    def addNum(self, num: int) -> None:
        # import heapq
        
        m = len(self.before)
        n = len(self.after)
        # m -> m + 1, 但是不直接插入, 而是先给after, 再返回给before
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

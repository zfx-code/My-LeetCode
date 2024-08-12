"""
264. 丑数 II
这是 LeetCode 上的「」, 难度为「中等」。

Tag : 「多路归并」、「堆」、「优先队列」

给你一个整数 n , 请你找出并返回第 n 个 丑数 。

丑数 就是只包含质因数 2、3 和 5 的正整数。

输入: n = 10

输出: 12

解释: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

1 <= n <= 1690

基本思路
根据丑数的定义, 我们有如下结论: 

(1) 1是最小的丑数。
(2) 对于任意一个丑数 , 其与任意的质因数(2, 3, 5)乘, 结果仍为丑数。
"""


class Solution:
    """
    优先队列（小根堆）
    有了基本的分析思路, 一个简单的解法是使用优先队列: 

    (1) 起始先将最小丑数1放入队列
    (2) 每次从队列取出最小值x, 然后将x所对应的丑数2x, 3x, 5x入队。
    (3) 对步骤(2)循环多次, 第n次出队的值即是答案。
    为了防止同一丑数多次进队, 我们需要使用数据结构set()来记录入过队列的丑数。

    时间复杂度: 优先队列pop: O(1), push: O(logn), 整体O(nlogn)
    空间复杂度: O(n)
    """
    def nthUglyNumber(self, n: int) -> int:
        from queue import PriorityQueue
        pq = PriorityQueue()
        hashtable = dict()

        pq.put(1)

        for _ in range(n - 1):
            ugly = pq.get()
            for i in [2, 3, 5]:
                if i * ugly not in hashtable:
                    hashtable[i * ugly] = 1 
                    pq.put(i * ugly)
        
        return pq.get()
    
    """
    多路归并(多指针)
    之后新产生的丑数都是基于已有x去乘上[2, 3, 5]
    所以可以根据当前的序列arr, 生成下一位丑数
    用3个指针指向arr下标, arr[i] * [2, 3, 5]表示使用到哪里了

    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def nthUglyNumber2(self, n: int) -> int:
        arr = [1]

        # 2, 3, 5
        i2, i3, i5 = 0, 0, 0
        
        for i in range(n - 1):
            a = arr[i2] * 2
            b = arr[i3] * 3
            c = arr[i5] * 5
            x = min(a, b, c)

            # 已经使用过/重复
            if x == a:
                i2 += 1
            
            if x == b:
                i3 += 1
            
            if x == c:
                i5 += 1
            
            arr.append(x)
        
        return arr[n - 1]


"""

代码


313. 超级丑数

超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

 

示例 1：

输入：n = 12, primes = [2,7,13,19]
输出：32 
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
示例 2：

输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
 
提示：

1 <= n <= 105
1 <= primes.length <= 100
2 <= primes[i] <= 1000
题目数据 保证 primes[i] 是一个质数
primes 中的所有值都 互不相同 ，且按 递增顺序 排列
"""

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 多路归并, 之后产生的丑数都是[基于已有丑数]*[质因子]
        # 有序序列arr, 丑数序列ans
        # primes长度m, 使用m个指针
        # 使用三元组(v, pi, ai), 表示v = primes[pi] * ans[ai]
        # 初始小根堆加入所有的(primes[pi], pi, 0), 每次取出最小的元素
        # 放入(ans[ai+1]*primes[pi], pi, ai+1)
        # 放入前去重最后一个ans[-1]
        from heapq import heappush, heappop, heapify
        m = len(primes)
        # 候选的下一个超级丑数
        q = [[primes[pi], pi, 0] for pi in range(m)]
        heapify(q)
 
        ans = [1]

        while len(ans) < n:
            v, pi, ai = heappop(q)
            # 依次增加最小的, 考虑去重
            if len(ans) == 0 or v != ans[-1]:
                ans.append(v)
            heappush(q, [ans[ai + 1] * primes[pi], pi, ai + 1])
        
        return ans[n - 1]
            




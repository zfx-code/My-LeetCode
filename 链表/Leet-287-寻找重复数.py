"""
287. 寻找重复数(关于有环链表找入环点的分析)

给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
"""

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        快慢指针(环形链表)
        nums范围是[1, n]
        将数组下标n和数nums[n]建立映射f(x)
        eg: [1,3,4,2]
        0->1, 1->3, 2->4, 3->2
        从下标0出发, 根据f(n)算出一个值, 将该值作为新的下标重复走f(n), 直到下标越界:
            0->1->3->2->4->None
        有重复数则存在环(不是双射)
        则找到重复数 <=> 找到环的入口

        slow = slow.next      => slow = nums[slow]
        fast = fast.next.next => fast = nums[nums[fast]]

        找入环点分析:

                ----<----
                |       |
        0 -->-- x -->-- y
        记作3段距离, 其中x是入环点, y是slow, fast第一次相遇的点
        0 -> x: a 
        x -> y: b 
        y -> x: c(注意是有方向的, c != b)
        
        分析走过的路程:
            slow: a + b(y相遇)
            fast: a + b + n(b + c)(比slow多走了n圈)
        有表达式: 2(a + b) = a + b + n(b + c)
        =>               a = c + (n - 1)(b + c)
        则表明, 除去绕的圈之外, 从起点0和交点y出发, 同时走可以到达入环点x
        因此需要重新把slow放到起点, 和fast一步一步走, 相遇则为入环点
        """

        slow, fast = 0, 0 
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # 有环必定相遇, 重新跑找到环入口
        slow = 0

        # 这次每次只跑一步 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

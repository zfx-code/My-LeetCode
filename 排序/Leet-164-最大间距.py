"""
164. 最大间距

给定一个无序的数组 nums，返回 数组在排序之后，相邻元素之间最大的差值 。如果数组元素个数小于 2，则返回 0 。

您必须编写一个在「线性时间」内运行并使用「线性额外空间」的算法。

示例 1:

输入: nums = [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: nums = [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
"""

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        if len(nums) == 2:
            return abs(nums[0] - nums[1])

        # 维护最大值和最小值
        minVal, maxVal = min(nums), max(nums) 

        if minVal == maxVal:
            return 0 
        
        # 相邻数字最大间距 >= (max - min) / (N - 1)向上取整
        # 反证法 AN - A1 = (N - 1)dx < max - min而一定是A1=min, AN=max矛盾
        # 桶的大小, 元素的最大间距不会出现在桶内部(一定是在相邻的桶)
        # max_1, min_2表示相邻的桶且相邻的排序差值
        # size = len(nums) + 1 
        # 桶的间隔
        d = 1 + (maxVal - minVal - 1) // (len(nums) - 1)
        print(d)
        size = 1 + (maxVal - minVal) // d
        bucket = [[-1, -1] for _ in range(size)]

        for x in nums:
            # 落在哪个桶
            idx = (x - minVal) // d 

            # 没有数, 直接覆盖
            if bucket[idx][0] == -1:
                bucket[idx][0] = x 
                bucket[idx][1] = x
            # 更新 
            else:
                bucket[idx][0] = min(bucket[idx][0], x)
                bucket[idx][1] = max(bucket[idx][1], x)
        
        print(bucket)
        # 取相邻桶的差值
        ans = 0 
        pre_max = inf
        for i in range(size):
            # 跳过这次判断
            if bucket[i][0] == -1:
                continue

            ans = max(ans, bucket[i][0] - pre_max)
            pre_max = bucket[i][1]

        return ans 
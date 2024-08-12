"""
二分

峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

示例 1：

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

提示：

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
对于所有有效的 i 都有 nums[i] != nums[i + 1]



    low - mid - high
    if   nums[mid] < nums[low],  mid左边一定有极大值
    elif nums[mid] < nums[high], mid右边一定有极大值
    elif nums[mid-1] < nums[mid] < nums[mid+1], 极大值在右边(增)
    else 单调减, 极大值在左边

    如果你往下坡方向走，也许可能遇到新的山峰，但是也许是一个一直下降的坡，最后到边界。但是如果你往上坡方向走，就算最后一直上的边界，由于最边界是负无穷，所以就一定能找到山峰，总的一句话，往递增的方向上，二分，一定能找到，往递减的方向只是可能找到，也许没有

【补充】理解二分，请牢记区间的定义！区间内的数（下标）都是还未确定与 target 的大小关系的，有的是 < target，有的是 ≥ target；区间外的数（下标）都是确定与 target 的大小关系的。
对于本题（递增数组），区间左侧外面的都是 < target，区间右侧外面的都是 ≥ target。从这个定义可以知道，找到了 ≥ target 的数之后，要把这个数（下标）放在区间外面，而不是区间里面！
所以对于闭区间写法，当 nums【mid】 >= target 时，要把 mid 放在区间外面，代码就自然是 right = mid - 1 了。

我是在看了这篇文章，https://blog.csdn.net/groovy2007/article/details/78309120，里那句“关键不在于区间里的元素具有什么性质，而是区间外面的元素具有什么性质。”之后醍醐灌顶，建立了我自己的二分查找心智模型，和up主的有些类似。

也就是看最终左右指针会停在哪里。
如果我们要找第一个大于等于x的位置，那么我就假设L最终会停在第一个大于等于x的位置，R停在L的左边。
这样按照上面那句话，可以把循环不变式描述为“L的左边恒小于x，R的右边恒大于等于x”，这样一来，其他的各种条件就不言自明了。
比如循环条件肯定是L小于R，因为我假设R停在L的左边。
而L和R转移的时候，根据循环不变式，如果mid小于x，肯定要令L等于mid+1，如果大于等于x，就令R等于mid-1。
"""


def findPeakElement(nums: list[int]) -> int:

    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        # 这是段递增区间, mid很可能就是结果
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        # 递减区间, 更新left: low - mid - high
        else:
            high = mid

    return high

# [bisect, bisect_right]: return first idx s.t. nums[idx] > x
# [bisect_left]         : return first idx s.t. nums[idx] >= x
# 如果找不到x, 则返回合适的插入点
# eg: [1,5,9,13,17] find(7) return 2 because [nums[1] < 7, nums[2] > 7]
# from bisect import bisect_left


"""
Leet-153. 寻找旋转排序数组中的最小值
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

这种是特殊返回了, 一定存在的情况下
需要判断到底是return low or high
"""
def findMin(nums: list[int]) -> int:
    low = 0 
    high = len(nums) - 1

    while low < high:
        mid = low + ((high - low) >> 1)

        # mid跟high一边
        if nums[mid] < nums[high]:
            high = mid 
        else:
            low = mid + 1
    
    # 此时low == high
    return nums[low]


"""
心得体会
更新通常是[low = mid(+1), high = mid(-1)]
到底这个+1, -1要不要, 实际上看的是比较的对象
就是得保证留下+1, -1之后, 解还在这个区间里
通常用谁来判断, 包含"="成立的那部分为True是不动的
eg: if nums[mid] <= target: 
        low = mid  # 不能 + 1, 很有可能丢掉这个解
    # 所以最好先判断 nums[mid] == target
    # 这样后边随便用+1, -1, 因为真正的解一定不在mid上

eg: 通常是更新mid的, 变体
if target <= nums[high] 成立的话, 说明要更新low
属于[low_new, high], high是留下来的(<=)
if target >= nums[low] 成立的话, 说明要更新high
属于[low, high_new], low是留下来的(<=)
"""
def search(nums: list[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        # method-2 调整两边
        while low <= high:
            
            mid = low + ((high - low) >> 1)
            
            print(low, high, mid)
            if nums[mid] == target:
                return mid 
            
            # low->mid不是一段递增区间
            if nums[mid] < nums[low]:
                # 在右边
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
            # 是一段递增区间, 正常判断
            else:
                if nums[low] <= target and nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1

nums = [1, 3] 
# print(search(nums=nums, target=3))
# # 

# print(findMin(nums=[4,5,6,7,0,1,2]))

from bisect import bisect_left

def twoSum(numbers: list[int], target: int) -> list[int]:
    # i = 0
    # j = 1
    for i in range(len(numbers) - 1):
        rem = target - numbers[i]
        j = i + 1 + bisect_left(numbers[i+1:], rem)
        print(i, j)
        if numbers[j] != numbers[i] and numbers[j] == rem:
            return [i + 1, j + 1]

print(twoSum([2,7,11,15], 9))



"""
2024.3.22

"""
import bisect
arr = [1,2,3,4,5]
# nums[j] >= x and nums[j-1] < x
j = bisect.bisect_left(arr, 6)

print(j)


# 实现在增序数组中二分查询, 第一个>=x的数的索引idx
# s.t. arr[idx - 1] < x <= arr[idx]
# nums[-1] < x, return len(arr)
def bisect_left_my(arr, x):
    low = 0
    # 希望用high保存结果 
    high = len(arr)

    while low < high:
        mid = low + ((high - low) >> 1)
        if arr[mid] >= x:
            high = mid 
        else:
            low = mid + 1 

    return high 

# 先判断你想要的区间, 通常是不动(+1, -1)
# 不想要的区间需要缩短(+1, -1)
# 实现在增序数组中二分查询, 第一个>x的数的索引idx
# s.t. arr[idx - 1] <= x < arr[idx]
# nums[-1] < x, return len(arr)
def bisect_right_my(arr, x):
    
    # 希望用low保存结果 
    low = 0
    
    high = len(arr)

    while low < high:
        mid = low + ((high - low) >> 1)
        if arr[mid] > x:
            high = mid 
        else:
            low = mid + 1 

    return high

x = 0
print("bisect:")
print(bisect.bisect_left(arr, x))
print("bisect_right:")
print(bisect.bisect_right(arr, x))

print("bisect_my:")
print(bisect_right_my(arr, x))
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if n == k:
            return arr 
        
        # 二分 + 双指针, O(k+log(n))
        # 直接二分是O(logn)
        # [low, low+k]与[high, high+k]都是合法区间
        low = 0 
        high = n - k

        # 最终low == high结束
        while low < high:
            mid = low + ((high - low) >> 1)
            # 二分左端点, 左边界差>右边界差 -> 往右边走
            # 其次不需要判断区间是否合法mid + k <= n, 保证mid不会>n
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1 
            # 注意小于等于, 此时mid是可以的
            else:
                high = mid
        
        return arr[low:low + k]
        

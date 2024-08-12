    
"""
求解逆序对

(1) 归并排序法
(2) 树状数组法
"""

class Solution:
    def reversePairs(self, record: list[int]) -> int:
        
        ans = 0
        # method1: 归并排序算逆序对
        # [low, high]闭区间

        # 闭区间[low, high]
        # 此时[low, mid], [mid + 1, high]都已经有序, 合并即可
        def merge(arr, low, mid, high):
            nonlocal ans 
            arr_tmp = []

            # i负责左边, j负责右边
            i, j = low, mid + 1 
            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    arr_tmp.append(arr[i])
                    i += 1 
                # 右边的j位置加入, 比[i, mid]的都小, 都算上
                else:
                    ans += mid - i + 1
                    arr_tmp.append(arr[j])
                    j += 1 
            # 剩余的加进来, 不用比了(只会剩1个)
            while i <= mid:
                arr_tmp.append(arr[i])
                i += 1 
            
            while j <= high:
                arr_tmp.append(arr[j])
                j += 1 

            # 覆盖原数组
            for k in range(high - low + 1):
                arr[low + k] = arr_tmp[k]

        # 合并
        def merge_sort(arr, low, high):
            mid = low + ((high - low) >> 1)
            if low < high:
                merge_sort(arr, low, mid)
                merge_sort(arr, mid + 1, high)
                merge(arr, low, mid, high)

        n = len(record)
        merge_sort(record, 0, n - 1)

        return ans
    
    def reversePairs_Tree_Arr(self, record: list[int]) -> int:
        def lowbit(x: int):
            return x & (-x)
        
        # 更新所有包含x的节点
        def update(tree_arr: list[int], x):
            while x < len(tree_arr):
                tree_arr[x] += 1 
                x           += lowbit(x)
        
        # 
        def count_x(tree_arr: list[int], x: int):
            res = 0 
            while x > 0:
                res += tree_arr[x]
                x   -= lowbit(x)
            
            return res

        ans = 0
        n = len(record)
        # 从大到小排序
        sorted_record = sorted(record, reverse=True)
        rank_map = {v : i for i, v in enumerate(sorted_record)}

        tree_arr = [0 for i in range(n + 1)]

        for i in range(n):
            x = rank_map[record[i]] + 1
            update(tree_arr, x)
            ans += count_x(tree_arr, x - 1)
        
        return ans

s = Solution()
record = [1,3,2,3,1]
record = [5,3,4,2,1]
# print(s.reversePairs_Tree_Arr(record))


# 离散化：绝对数值转秩次【rank从0开始】
nums = record
uniques = sorted(set(nums), reverse=True)
rank_map = {v:i for i,v in enumerate(uniques)}

# n = len(nums)
# # print(rank_map)
# for i in range(n-1, -1, -1):
#     rank = rank_map[nums[i]]    # 当前值的排名
#     print(rank + 1)
#     # tree.add(rank, 1)           # 单点更新+1
#     # ans += tree.query(rank-1)    # 查询 当前排名之前 的元素有多少个


# print(uniques)

print(rank_map)

d = sorted([i + 1 for i in range(len(record))], key=lambda x: record[x - 1], reverse=True)
for i in record:
    print(d[i - 1])